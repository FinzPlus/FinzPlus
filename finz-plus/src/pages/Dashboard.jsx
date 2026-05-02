/* 📂 ARCHIVO: src/pages/Dashboard.jsx */
import React, { useState, useEffect } from 'react';
import { finzService } from '../services/finzService';
import FormularioMovimiento from '../components/FormularioMovimiento';

export default function Dashboard() {
    const [movimientos, setMovimientos] = useState([]);
    const [usuario] = useState(finzService.obtenerUsuario());

    const cargarDatos = () => {
        const datos = finzService.obtenerMovimientos();
        setMovimientos(datos);
    };

    useEffect(() => {
        cargarDatos();
    }, []);

    // --- LÓGICA DE CÁLCULO REAL ---
    // Sumamos todos los montos de la lista de movimientos
    const saldoTotal = movimientos.reduce((acc, mov) => acc + mov.monto, 0);
    
    // Formateador de moneda para que se vea profesional (Pesos Colombianos)
    const formatoMoneda = (valor) => {
        return new Intl.NumberFormat('es-CO', {
            style: 'currency',
            currency: 'COP',
            minimumFractionDigits: 0
        }).format(valor);
    };

    return (
        <div className="container py-4">
            <div className="row mb-4">
                <div className="col">
                    <h1 className="text-primary">Panel Finz+</h1>
                    <p className="lead">Bienvenido, <strong>{usuario?.nombres || 'Usuario'}</strong></p>
                </div>
            </div>

            <FormularioMovimiento alGuardar={cargarDatos} />

            <div className="row">
                {/* Saldo Actual Dinámico */}
                <div className="col-md-4 mb-4">
                    <div className={`card text-white shadow ${saldoTotal >= 0 ? 'bg-success' : 'bg-warning'}`}>
                        <div className="card-body">
                            <h5 className="card-title">Saldo Disponible</h5>
                            <h2 className="card-text">{formatoMoneda(saldoTotal)}</h2>
                            <small>{saldoTotal < 0 ? '¡Cuidado con los gastos!' : 'Vas por buen camino'}</small>
                        </div>
                    </div>
                </div>

                {/* Metas - HU10 */}
                <div className="col-md-4 mb-4">
                    <div className="card text-white bg-info shadow">
                        <div className="card-body">
                            <h5 className="card-title">Meta: Ahorro Carro</h5>
                            <div className="progress mt-2" style={{height: '20px'}}>
                                <div className="progress-bar bg-warning" style={{width: '65%'}}>65%</div>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Deudas - HU11 */}
                <div className="col-md-4 mb-4">
                    <div className="card text-white bg-danger shadow">
                        <div className="card-body">
                            <h5 className="card-title">Deudas Pendientes</h5>
                            <h2 className="card-text">$ 850.000</h2>
                        </div>
                    </div>
                </div>
            </div>

            {/* Tabla de Transacciones */}
            <div className="row">
                <div className="col-12">
                    <div className="card shadow">
                        <div className="card-header bg-white">
                            <h5 className="mb-0">Historial de Movimientos</h5>
                        </div>
                        <div className="card-body">
                            <table className="table table-hover">
                                <thead>
                                    <tr>
                                        <th>Descripción</th>
                                        <th>Categoría</th>
                                        <th>Monto</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {movimientos.length > 0 ? (
                                        movimientos.map((m) => (
                                            <tr key={m.id}>
                                                <td>{m.descripcion}</td>
                                                <td><span className="badge bg-secondary">{m.categoria}</span></td>
                                                <td className={m.monto < 0 ? 'text-danger' : 'text-success'}>
                                                    {formatoMoneda(m.monto)}
                                                </td>
                                            </tr>
                                        ))
                                    ) : (
                                        <tr>
                                            <td colSpan="3" className="text-center text-muted py-4">
                                                No hay movimientos aún.
                                            </td>
                                        </tr>
                                    )}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}