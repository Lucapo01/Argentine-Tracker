import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import "./Header.css"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars } from '@fortawesome/free-solid-svg-icons'

const Header = ({ toggleMenu }) => {
    const [headerStyle, setHeaderStyle] = useState('light')
    const navigate = useNavigate()

    useEffect(() => {
        const onScroll = () => {
            if (window.scrollY >= 100) {
                setHeaderStyle("")
            } else {
                setHeaderStyle("light")
            }
        };
    
        window.addEventListener("scroll", onScroll);
    
        // Limpia el listener al desmontar el componente
        return () => {
          window.removeEventListener('scroll', onScroll);
        };
      }, []);

    const onScroll = () => {
        if (window.scrollY >= 100) {
            setHeaderStyle("")
        } else {
            setHeaderStyle("light")
        }
    };

    window.addEventListener("scroll", onScroll);

    return (
        <div className={`header ${headerStyle}`}>
            <FontAwesomeIcon icon={faBars} className='bars' onClick={() => toggleMenu()} />
            <div className='title-container' onClick={() => navigate('/graph/1')}>
                <img alt='' src={window.location.origin + '/logo.png'} className='icon' />
                <h1 className='title'>FCI Tracker</h1>
                <div className='beta'>
                    <h5>(Beta)</h5>
                </div>
            </div>
        </div>
    )
}

export default Header