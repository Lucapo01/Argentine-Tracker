import React from 'react'
import './Tickers.css'

const Ticker = ({id, name, selectTicker, selected}) => {
  return (
    <div className={id === selected ? 'ticker selected' : 'ticker'} onClick={() => selectTicker(id)}>{name}</div>
  )
}

export default Ticker