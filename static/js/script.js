// Scripts personalizados para ElectroniStock

// Inicialización cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function () {
    initializeApp();
});

function initializeApp() {
    // Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Inicializar popovers de Bootstrap
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Animaciones de fade-in para cards
    observeCards();

    // Validación de formularios
    setupFormValidation();

    // Auto-focus en campos de búsqueda
    focusSearchFields();

    // Confirmaciones de acciones peligrosas
    setupDangerousActions();
}

// Observador para animaciones de cards
function observeCards() {
    const cards = document.querySelectorAll('.card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, {
        threshold: 0.1
    });

    cards.forEach(card => {
        observer.observe(card);
    });
}

// Validación de formularios
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();

                // Mostrar mensaje de error
                showAlert('Por favor, completa todos los campos requeridos.', 'danger');
            }
            form.classList.add('was-validated');
        });
    });
}

// Auto-focus en campos de búsqueda
function focusSearchFields() {
    const searchInputs = document.querySelectorAll('input[type="search"], input[name="q"]');
    searchInputs.forEach(input => {
        if (!input.value && input.offsetParent !== null) {
            input.focus();
        }
    });
}

// Configurar acciones peligrosas
function setupDangerousActions() {
    const dangerousButtons = document.querySelectorAll('.btn-danger');
    dangerousButtons.forEach(button => {
        if (!button.hasAttribute('onclick')) {
            button.addEventListener('click', function (e) {
                e.preventDefault();
                const action = this.getAttribute('data-action') || 'realizar esta acción';
                if (confirm(`¿Estás seguro de que deseas ${action}?`)) {
                    // Proceder con la acción
                    if (this.closest('form')) {
                        this.closest('form').submit();
                    }
                }
            });
        }
    });
}

// Función para mostrar alertas dinámicas
function showAlert(message, type = 'info', duration = 5000) {
    const alertContainer = document.querySelector('.container');
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    // Insertar al inicio del container
    alertContainer.insertBefore(alertDiv, alertContainer.firstChild);

    // Auto-remover después del tiempo especificado
    setTimeout(() => {
        if (alertDiv && alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, duration);
}

// Función para formatear números como moneda
function formatCurrency(amount) {
    return new Intl.NumberFormat('es-MX', {
        style: 'currency',
        currency: 'MXN'
    }).format(amount);
}

// Función para formatear fechas
function formatDate(dateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('es-MX', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }).format(date);
}

// Función para validar stock y mostrar indicadores
function updateStockIndicators() {
    const stockElements = document.querySelectorAll('[data-stock]');
    stockElements.forEach(element => {
        const stock = parseInt(element.getAttribute('data-stock'));
        let className, icon, text;

        if (stock <= 10) {
            className = 'text-danger';
            icon = '⚠️';
            text = 'Stock bajo';
        } else if (stock <= 50) {
            className = 'text-warning';
            icon = '⚠️';
            text = 'Stock medio';
        } else {
            className = 'text-success';
            icon = '✓';
            text = 'Stock bueno';
        }

        element.className = `badge ${className}`;
        element.innerHTML = `${icon} ${stock} ${text}`;
    });
}

// Función para búsqueda en tiempo real (opcional)
function setupLiveSearch() {
    const searchInput = document.getElementById('liveSearch');
    if (!searchInput) return;

    let searchTimeout;
    searchInput.addEventListener('input', function () {
        clearTimeout(searchTimeout);
        const query = this.value.trim();

        if (query.length >= 2) {
            searchTimeout = setTimeout(() => {
                performLiveSearch(query);
            }, 300);
        }
    });
}

function performLiveSearch(query) {
    fetch(`/api/componentes?search=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            displaySearchResults(data);
        })
        .catch(error => {
            console.error('Error en búsqueda:', error);
        });
}

function displaySearchResults(results) {
    const resultsContainer = document.getElementById('searchResults');
    if (!resultsContainer) return;

    if (results.length === 0) {
        resultsContainer.innerHTML = '<p class="text-muted">No se encontraron resultados.</p>';
        return;
    }

    const html = results.map(item => `
        <div class="card mb-2">
            <div class="card-body py-2">
                <h6 class="mb-1">${item.nombre}</h6>
                <small class="text-muted">${item.descripcion || 'Sin descripción'}</small>
                <div class="float-end">
                    <span class="badge bg-primary">${formatCurrency(item.precio)}</span>
                    <span class="badge bg-secondary">${item.stock} unidades</span>
                </div>
            </div>
        </div>
    `).join('');

    resultsContainer.innerHTML = html;
}

// Función para exportar datos a CSV
function exportToCSV(data, filename) {
    const csvContent = "data:text/csv;charset=utf-8,"
        + data.map(row => row.join(",")).join("\n");

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Función para copiar al portapapeles
async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        showAlert('Texto copiado al portapapeles', 'success', 2000);
    } catch (err) {
        console.error('Error al copiar al portapapeles:', err);
        showAlert('Error al copiar al portapapeles', 'danger', 3000);
    }
}

// Función para imprimir página
function printPage() {
    window.print();
}

// Función para toggle de tema oscuro (futuro)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDark);
}

// Cargar preferencia de tema
function loadThemePreference() {
    const isDark = localStorage.getItem('darkMode') === 'true';
    if (isDark) {
        document.body.classList.add('dark-mode');
    }
}

// Utilidades para manejo de errores
function handleAjaxError(xhr, status, error) {
    console.error('Error AJAX:', status, error);
    showAlert('Ocurrió un error al procesar la solicitud.', 'danger');
}

// Función para confirmar eliminación con más detalles
function confirmarEliminacionDetallada(id, nombre, tipo = 'componente') {
    const mensaje = `¿Estás seguro de que deseas eliminar el ${tipo} "${nombre}"?\n\nEsta acción no se puede deshacer.`;

    if (confirm(mensaje)) {
        // Mostrar indicador de carga
        const button = event.target.closest('button');
        const originalHTML = button.innerHTML;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Eliminando...';
        button.disabled = true;

        // Simular delay y luego proceder
        setTimeout(() => {
            window.location.href = `/${tipo}s/eliminar/${id}`;
        }, 1000);
    }
}

// Validación personalizada para campos numéricos
function validateNumericInput(input, min = 0, max = null) {
    const value = parseFloat(input.value);

    if (isNaN(value) || value < min) {
        input.setCustomValidity(`El valor debe ser mayor o igual a ${min}`);
        return false;
    }

    if (max !== null && value > max) {
        input.setCustomValidity(`El valor debe ser menor o igual a ${max}`);
        return false;
    }

    input.setCustomValidity('');
    return true;
}

// Configurar validadores numéricos
document.addEventListener('DOMContentLoaded', function () {
    const numericInputs = document.querySelectorAll('input[type="number"]');
    numericInputs.forEach(input => {
        input.addEventListener('input', function () {
            const min = parseFloat(this.getAttribute('min')) || 0;
            const max = parseFloat(this.getAttribute('max')) || null;
            validateNumericInput(this, min, max);
        });
    });
});

// Función para resaltar términos de búsqueda
function highlightSearchTerms(text, terms) {
    if (!terms || !text) return text;

    const regex = new RegExp(`(${terms.split(' ').join('|')})`, 'gi');
    return text.replace(regex, '<mark class="search-highlight">$1</mark>');
}

// Exportar funciones globales para uso en templates
window.ElectroniStock = {
    showAlert,
    formatCurrency,
    formatDate,
    copyToClipboard,
    exportToCSV,
    printPage,
    toggleDarkMode,
    confirmarEliminacionDetallada,
    highlightSearchTerms
};