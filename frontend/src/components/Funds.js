import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import './Funds.css'

const Funds = () => {
    const { id } = useParams()
    const { date } = useParams()
    const [totalFunds, setTotalFunds] = useState({})

    useEffect(() => {
        const fetchFunds = async () => {
            const res = await fetch(`http://localhost:8000/point/${id}/${date}`)
            const data = await res.json()
            setTotalFunds(data)
        }

        fetchFunds()
    }, [id, date])

    return (
        <>
            {Object.keys(totalFunds).length > 0 &&
                <div className='funds-container'>
                    <div>
                        <h3>Fecha: {date}</h3>
                        <h3>Precio: {totalFunds.price}</h3>
                    </div>
                    <div className='funds'>
                        <h4 className='fund'>Fondo</h4>
                        <h4 className='fund'>Cantidad</h4>
                        {Object.keys(totalFunds.funds).map((fund, index) => (
                            <React.Fragment key={fund}>
                                <h4 className='fund'>{fund}</h4>
                                <h4 className='fund'>{totalFunds.funds[fund]}</h4>
                            </React.Fragment>
                        ))}
                    </div>
                </div>
            }
        </>
    )
}

export default Funds