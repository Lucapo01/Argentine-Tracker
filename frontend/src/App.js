import { useState, useEffect } from 'react'
import './App.css'
import Header from './components/Header'
import Tickers from './components/Tickers';
import LineChart from './components/LineChart';

function App() {
    const [tickers, setTickers] = useState({})

    useEffect(() => {
        const getTickers = async () => {
            const tickersFromServer = await fetchTickers()
            setTickers(tickersFromServer)
        }

        getTickers()
    }, [])

    const fetchTickers = async () => {
        const res = await fetch('Access-Control-Allow-Origin: http://localhost:8000/tickers/')
        const data = await res.json()
        return data
    }

    const [selected, setSelected] = useState('1')

    const selectTicker = (id) => {
        setSelected(id)
    }

    return (
        <>
            <Header title='FCI Tracker' />
            <div className='container'>
                <Tickers tickers={tickers} selectTicker={selectTicker} selected={selected} />
                <LineChart />
            </div>
        </>
    );
}

export default App;