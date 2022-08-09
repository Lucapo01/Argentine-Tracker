import React from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import "./Header.css"
import PropTypes from 'prop-types'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars } from '@fortawesome/free-solid-svg-icons'

const Header = ({ title, toggleMenu }) => {
    const location = useLocation()
    const navigate = useNavigate()

    return (
        <div className='header'>
            {location.pathname === '/' && <FontAwesomeIcon icon={faBars} className='bars' onClick={() => toggleMenu()}/>}
            <div className='title-container' onClick={() => navigate('/')}>
                <img alt='' src={process.env.PUBLIC_URL + "favicon.ico"} className='icon'/>
                <h1 className='title'>{title}</h1>
            </div>
        </div>
    )
}

Header.propTypes = {
    title: PropTypes.string.isRequired
}

export default Header