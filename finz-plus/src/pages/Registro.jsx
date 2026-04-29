/* 📂 ARCHIVO: src/pages/Registro.jsx */
import React from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom'; // <--- 1. Importamos el "trasladista"
import { finzService } from '../services/finzService';

export default function Registro() {
    const { register, handleSubmit, formState: { errors } } = useForm();
    const navigate = useNavigate(); // <--- 2. Inicializamos la función de navegación

    const alEnviar = (datos) => {
        console.log("Datos capturados:", datos);
        finzService.guardarUsuario(datos);
        
        // 3. Traslado automático al Dashboard después de guardar
        alert("¡Bienvenido a Finz+!");
        navigate('/dashboard'); 
    };

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-6">
                    <form onSubmit={handleSubmit(alEnviar)} className="card p-4 shadow border-primary">
                        <h2 className="text-center text-primary mb-4">Registro Finz+</h2>
                        
                        <div className="mb-3">
                            <label className="form-label">Nombres Completos</label>
                            <input 
                                {...register("nombres", { required: "El nombre es obligatorio" })} 
                                className={`form-control ${errors.nombres ? 'is-invalid' : ''}`}
                            />
                        </div>

                        <div className="mb-3">
                            <label className="form-label">Documento</label>
                            <input 
                                type="number"
                                {...register("documento", { required: "Documento requerido" })} 
                                className="form-control"
                            />
                        </div>

                        <button type="submit" className="btn btn-primary w-100 mt-3">
                            Crear mi cuenta y entrar
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}