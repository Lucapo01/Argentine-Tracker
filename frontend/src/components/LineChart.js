import { React, useState, useEffect } from 'react'
import { Line } from 'react-chartjs-2'
/* eslint-disable no-unused-vars */
import { Chart as ChartJS } from 'chart.js/auto'
import './LineChart.css'

const LineChart = ({ selectedId }) => {
    const [ticker, setTicker] = useState({
        "id": 0,
        "name": "",
        "funds": {
            "total": {}
        },
        "price": 0,
        "type": ""
    })

    useEffect(() => {
        const fetchTicker = async (id) => {
            const res = await fetch(`http://localhost:8000/tickers/${id}`)
            const data = await res.json()
            setTicker(data)
        }

        fetchTicker(selectedId)
    }, [selectedId])

    const openDetail = async (element) => {
        if (element.length > 0) {
            const date = ticker.funds.total.dates[element[0].index]
            window.open(`/${selectedId}/${date}`, '_blank', 'noopener,noreferrer');
        }
    }

    const data = {
        labels: ticker.funds.total.dates,
        datasets: [{
            label: ticker.name,
            data: ticker.funds.total.qty,
            borderColor: 'rgba(0, 98, 255, 1)',
            borderWidth: 1,
            pointBackgroundColor: 'rgba(0, 98, 255, 1)',
            pointRadius: 6,
            pointHoverRadius: 8,
            pointHoverBackgroundColor: 'rgba(0, 98, 255, 1)',
            fill: false,
            tension: 0
        }]
    }

    return (
        <div className='line-chart'>
            <Line
                data={data}
                options={{
                    scales: {
                        y: {
                            ticks: {
                                color: '#000000',
                                font: {
                                    size: 14,
                                    weight: 'bolder'
                                }
                            },
                            grid: {
                                color: '#404040'
                            }
                        },
                        x: {
                            ticks: {
                                color: '#000000',
                                font: {
                                    size: 14,
                                    weight: 'bolder'
                                }
                            },
                            grid: {
                                color: '#404040'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: ticker.name,
                            color: '#000000',
                            font: {
                                size: 18
                            }
                        },
                        legend: {
                            display: false
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: true,
                            titleFont: {
                                size: 16
                            },
                            bodyFont: {
                                size: 12
                            },
                            callbacks: {
                                title: (context) => {
                                    return context[0].label
                                },
                                label: (context) => {
                                    const newLineArray = []
                                    const index = context.dataIndex
                                    newLineArray.push(`Cantidad: ${context.dataset.data[index].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`)
                                    newLineArray.push(`Precio: ${ticker.funds.total.prices[index].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`)
                                    return newLineArray
                                }
                            },
                            displayColors: false
                        }
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    onClick: (evt, element) => openDetail(element)
                }}
            />
        </div>
    )
}

export default LineChart