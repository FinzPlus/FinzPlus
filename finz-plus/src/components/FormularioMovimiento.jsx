/* 📂 ARCHIVO: src/components/FormularioMovimiento.jsx */
import React, { useRef } from 'react';
import { finzService } from '../services/finzService';

export default function FormularioMovimiento({ alGuardar }) {
    // Usamos useRef para capturar los valores sin que la pantalla recargue en cada letra
    const descRef = useRef();
    const montoRef = useRef();
    const catRef = useRef();

    const manejarEnvio = (e) => {
        e.preventDefault();
        
        const nuevoMov = {
            descripcion: descRef.current.value,
            monto: parseFloat(montoRef.current.value),
            categoria: catRef.current.value,
            tipo: montoRef.current.value < 0 ? 'egreso' : 'ingreso'
        };

        if (!nuevoMov.descripcion || !nuevoMov.monto) return alert("Llena los campos");

        finzService.guardarMovimiento(nuevoMov);
        alGuardar(); // Esta función avisará al Dashboard que debe refrescarse

        // Limpiamos los campos quirúrgicamente
        descRef.current.value = "";
        montoRef.current.value = "";
    };

    return (
        <form onSubmit={manejarEnvio} className="card p-3 mb-4 border-info">
            <h6 className="text-info">Registrar Nuevo Movimiento</h6>
            <div className="row g-2">
                <div className="col-md-5">
                    <input ref={descRef} type="text" className="form-control" placeholder="¿En qué gastaste?" />
                </div>
                <div className="col-md-3">
                    <input ref={montoRef} type="number" className="form-control" placeholder="Monto (usa - para gastos)" />
                </div>
                <div className="col-md-2">
                    <select ref={catRef} className="form-select">
                        <option value="Alimentación">Alimentación</option>
                        <option value="Transporte">Transporte</option>
                        <option value="Hogar">Hogar</option>
                        <option value="Ocio">Ocio</option>
                    </select>
                </div>
                <div className="col-md-2">
                    <button type="submit" className="btn btn-info w-100 text-white">Añadir</button>
                </div>
            </div>
        </form>
    );
}