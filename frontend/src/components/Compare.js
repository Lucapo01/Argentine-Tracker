import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import './Compare.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowDown} from '@fortawesome/free-solid-svg-icons'

const Compare = () => {
    const { id } = useParams()
    const { date1 } = useParams()
    const { date2 } = useParams()
    const [compareData, setCompareData] = useState({})
    const [fundsList, setFundsList] = useState([])
    const [qtyDescendingOrder, setQtyDescendingOrder] = useState(true)

    useEffect(() => {
        const fetchFunds = async () => {
            const res = await fetch(`http://localhost:8000/compare/${id}/${date1}/${date2}`)
            const data = await res.json()
            setCompareData(data)

            const fundsListFromServer = data.table.slice(3)
            fundsListFromServer.sort((first, second) => {
                return second[3] - first[3];
            })
            setFundsList(fundsListFromServer)
        }

        fetchFunds()
    }, [id, date1, date2])

    const changeFundsListOrder = () => {
        setQtyDescendingOrder(!qtyDescendingOrder)
        const qtyDescendingOrderAux = !qtyDescendingOrder
        if (qtyDescendingOrderAux) {
            fundsList.sort((first, second) => {
                return second[3] - first[3];
            })
        } else {
            fundsList.sort((first, second) => {
                return first[3] - second[3];
            })
        }
    }

    return (
        <>
            {Object.keys(compareData).length > 0 &&
                <div className='compare-container'>
                    <div className='compare-initial-data'>
                        <h2>{compareData.name}</h2>
                        <h2>Fechas: {compareData.date}</h2>
                        <h2>Precio: {compareData.price}</h2>
                    </div>
                    <div className='compare-grid'>
                        <h5 className='compare-data'>Fondo</h5>
                        <h5 className='compare-data'>{date1}</h5>
                        <h5 className='compare-data'>{date2}</h5>
                        <h5 className='compare-data' onClick={() => changeFundsListOrder()}>
                            Qty Delta
                            <FontAwesomeIcon icon={faArrowDown} className={qtyDescendingOrder ? 'arrow' : 'arrow rotated'}/>
                            </h5>
                        <h5 className='compare-data'>% Delta</h5>
                        <h5 className='compare-data'>Total</h5>
                        <h5 className='compare-data'>{compareData.table[1][1]}</h5>
                        <h5 className='compare-data'>{compareData.table[1][2]}</h5>
                        <h5 className='compare-data'>{compareData.table[1][3]}</h5>
                        <h5 className='compare-data'>{compareData.table[1][4]}</h5>
                        <h5 className='compare-data'>Promedio</h5>
                        <h5 className='compare-data'>{compareData.table[2][1]}</h5>
                        <h5 className='compare-data'>{compareData.table[2][2]}</h5>
                        <h5 className='compare-data'>{compareData.table[2][3]}</h5>
                        <h5 className='compare-data'>{compareData.table[2][4]}</h5>
                        {fundsList.map((fund, index) => (
                            fund.map((data, index) => (
                                <h5 key={index} className='compare-data'>{data}</h5>
                            ))
                        ))}
                    </div>
                </div>
            }
        </>
    )
}

export default Compare