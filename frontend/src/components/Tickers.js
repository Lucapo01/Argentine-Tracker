import React from 'react'
import { useState, useEffect } from 'react'
import Ticker from './Ticker'
import './Tickers.css'

const Tickers = ({ selectTicker, selected, tickersMenu, toggleMenu }) => {
    const [tickers, setTickers] = useState({})
    const [searchTicker, setSearchTicker] = useState('')

    useEffect(() => {
        const fetchTickers = async () => {
            const res = await fetch(`http://${process.env.REACT_APP_PORT}/tickers/`)
            const data = await res.json()
            setTickers(data)
        }

        fetchTickers()
    }, [])

    return (
        <div className={tickersMenu ? 'tickers tickers-menu-active' : 'tickers'}>
            <input className='search' type="text" placeholder='Buscar' onChange={(event) => {
                setSearchTicker(event.target.value)
            }} />
            {Object.keys(tickers).filter((id) => {
                if (searchTicker === '') {
                    return id
                } else if (tickers[id].toUpperCase().includes(searchTicker.toUpperCase())) {
                    return id
                } return ''
            }).map((id, index) => (
                <Ticker key={id} id={id} name={tickers[id]} selectTicker={selectTicker} selected={selected} toggleMenu={toggleMenu} />
            ))}
        </div>
    )
}

export default Tickers