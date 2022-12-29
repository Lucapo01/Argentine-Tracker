import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import './Compare.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowDown } from '@fortawesome/free-solid-svg-icons'

const Compare = () => {
    const { id } = useParams()
    const { date1 } = useParams()
    const { date2 } = useParams()
    const [compareData, setCompareData] = useState({})
    const [fundsList, setFundsList] = useState([])
    const [descending, setDescending] = useState(true)
    const [sortedColumn, setSortedColumn] = useState(3)

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

    const sortByColumn = (column) => {
        if (descending) {
            const sorted = [...fundsList].sort((first, second) =>
                first[column] > second[column] ? 1 : -1
            )
            setFundsList(sorted)
            setDescending(!descending)
        } else {
            const sorted = [...fundsList].sort((first, second) =>
                first[column] < second[column] ? 1 : -1
            )
            setFundsList(sorted)
            setDescending(!descending)
        }
        setSortedColumn(column)
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
                        <h5 className='compare-data' onClick={() => sortByColumn(0)}>
                            Fondo
                            {sortedColumn === 0 &&
                                <FontAwesomeIcon icon={faArrowDown} className={descending ? 'arrow' : 'arrow rotated'} />
                            }
                        </h5>
                        <h5 className='compare-data' onClick={() => sortByColumn(1)}>
                            {date1}
                            {sortedColumn === 1 &&
                                <FontAwesomeIcon icon={faArrowDown} className={descending ? 'arrow' : 'arrow rotated'} />
                            }
                        </h5>
                        <h5 className='compare-data' onClick={() => sortByColumn(2)}>
                            {date2}
                            {sortedColumn === 2 &&
                                <FontAwesomeIcon icon={faArrowDown} className={descending ? 'arrow' : 'arrow rotated'}/>
                            }
                            </h5>
                        <h5 className='compare-data' onClick={() => sortByColumn(3)}>
                            Qty Delta
                            {sortedColumn === 3 &&
                                <FontAwesomeIcon icon={faArrowDown} className={descending ? 'arrow' : 'arrow rotated'}/>
                            }
                        </h5>
                        <h5 className='compare-data' onClick={() => sortByColumn(4)}>
                            % Delta
                            {sortedColumn === 4 &&
                                <FontAwesomeIcon icon={faArrowDown} className={descending ? 'arrow' : 'arrow rotated'}/>
                            }
                            </h5>
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