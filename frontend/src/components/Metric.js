import React from 'react'
import './Metric.css'

const Metric = ({ title, tickers }) => {
    const changeColor = (data) => {
        const style = { color: '' }
        if (data < 0) {
            style['color'] = 'rgb(220, 0, 0)'
        } else if (data > 0) {
            style['color'] = 'green'
        } else {
            style['color'] = 'black'
        }
        return style
    }

    const roundPercentage = (percentage) => {
        return (percentage * 100).toFixed(2)
    }

    const openTicker = (id) => {
        window.open(`/graph/${id}`, '_self', 'noopener,noreferrer')
    }

    return (
        <div className='metric'>
            <h4>{title}</h4>
            <div className='metric-row metric-atributes'>
                <p>Name</p>
                <p>Delta %</p>
            </div>
            {tickers.map((ticker) => (
                <div key={ticker.id} className='metric-row' onClick={() => openTicker(ticker.id)}>
                    <p>{ticker.name}</p>
                    <p style={changeColor(ticker.delta)}>{roundPercentage(ticker.delta)}</p>
                </div>
            ))}
        </div>
    )
}

export default Metric