import React from 'react'
import { Chart, LineController, LineElement, PointElement, LinearScale, Title, CategoryScale } from 'chart.js'
import { Line } from 'react-chartjs-2'
import './LineChart.css'

Chart.register(LineController, LineElement, PointElement, LinearScale, Title, CategoryScale);

const LineChart = ({ticker, name}) => {
    const data = {
        labels: ticker.dates,
        datasets: [{
            label: name,
            data: ticker.qty,
            borderColor: '#00ab14',
            borderWidth: 1,
            tension: 0.1
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
                                    color: '#ebebeb'
                                },
                                grid: {
                                    color: '#404040'
                                },
                                beginAtZero: true
                            },
                            x: {
                                ticks: {
                                    color: '#ebebeb'
                                },
                                grid: {
                                    color: '#404040'
                                }
                            }
                        }
                    }
                }
            />
        </div>
    )
}

export default LineChart