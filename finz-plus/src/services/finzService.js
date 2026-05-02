/* 📂 ARCHIVO: src/services/finzService.js */

// Nombres de las "tablas" en la memoria del navegador
const KEYS = {
    USUARIO: 'finz_usuario',
    MOVIMIENTOS: 'finz_movimientos',
    METAS: 'finz_metas',
    DEUDAS: 'finz_deudas'
};

export const finzService = {
    // --- HU 05: Usuarios (Registro/Login) ---
    guardarUsuario: (datos) => {
        localStorage.setItem(KEYS.USUARIO, JSON.stringify(datos));
    },
    obtenerUsuario: () => {
        return JSON.parse(localStorage.getItem(KEYS.USUARIO));
    },

    // --- HU 08 y 09: Transacciones y Cuentas ---
    obtenerMovimientos: () => {
        return JSON.parse(localStorage.getItem(KEYS.MOVIMIENTOS) || '[]');
    },
    guardarMovimiento: (movimiento) => {
        const actuals = finzService.obtenerMovimientos();
        actuals.push({ ...movimiento, id: Date.now() });
        localStorage.setItem(KEYS.MOVIMIENTOS, JSON.stringify(actuals));
    },

    // --- HU 10 y 11: Metas y Deudas ---
    obtenerMetas: () => JSON.parse(localStorage.getItem(KEYS.METAS) || '[]'),
    obtenerDeudas: () => JSON.parse(localStorage.getItem(KEYS.DEUDAS) || '[]'),

    // --- Preparación para el Futuro (Fetch) ---
    // Aquí es donde luego conectaremos con tu Backend de Maven
    sincronizarConServidor: async (datos) => {
        console.log("Listo para conectar con Spring Boot...");
    }
};