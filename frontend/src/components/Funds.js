import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import './Funds.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowDown} from '@fortawesome/free-solid-svg-icons'

const Funds = () => {
    const { id } = useParams()
    const { date } = useParams()
    const [totalFunds, setTotalFunds] = useState({})
    const [fundsList, setFundsList] = useState({})
    const [descendingOrder, setDescendingOrder] = useState(true)

    useEffect(() => {
        const fetchFunds = async () => {
            const res = await fetch(`http://localhost:8000/point/${id}/${date}`)
            const data = await res.json()
            setTotalFunds(data)
            const fundsListFromServer = Object.keys(data.funds).map((key) => {return [key, data.funds[key]]})
            fundsListFromServer.sort((first, second) => {
                return second[1] - first[1];
            })
            setFundsList(fundsListFromServer)
        }

        fetchFunds()
    }, [id, date])

    const changeFundsListOrder = () => {
        setDescendingOrder(!descendingOrder)
        const desendingOrderAux = !descendingOrder
        if (desendingOrderAux) {
            fundsList.sort((first, second) => {
                return second[1] - first[1];
            })
        } else {
            fundsList.sort((first, second) => {
                return first[1] - second[1];
            })
        }
    }

    return (
        <>
            {Object.keys(totalFunds).length > 0 &&
                <div className='funds-container'>
                    <div className='funds-initial-data'>
                        <h2>{totalFunds.name}</h2>
                        <h2>Fecha: {date}</h2>
                        <h2>Precio: {totalFunds.price}</h2>
                        <h2>Total: {totalFunds.total}</h2>
                        <h2>Promedio: {totalFunds.avg}</h2>
                    </div>
                    <div className='funds-grid'>
                        <h4 className='fund'>Fondo</h4>
                        <h4 className='fund' onClick={() => changeFundsListOrder()}>
                            Cantidad
                            <FontAwesomeIcon icon={faArrowDown} className={descendingOrder ? 'arrow' : 'arrow rotated'}/>
                            </h4>
                        {fundsList.map((fund) => (
                            <React.Fragment key={fund}>
                                <h4 className='fund'>{fund[0]}</h4>
                                <h4 className='fund'>{fund[1]}</h4>
                            </React.Fragment>
                        ))}
                    </div>
                </div>
            }
        </>
    )
}

export default Funds