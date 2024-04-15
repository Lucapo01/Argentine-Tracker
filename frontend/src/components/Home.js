import React, { useEffect, useRef, useState } from 'react'
import './Home.css'
import welcomeImg from './images/welcome.png'
import menuImg from './images/menu.PNG'
import graphImg from './images/grafico.PNG'
import totalAndAvgImg from './images/total y promedio.PNG'
import pointImg from './images/point.PNG'
import compareImg from './images/comparar.PNG'
import categoryImg from './images/categorias.PNG'
import donwloadImg from './images/descargar.PNG'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAngleDown } from '@fortawesome/free-solid-svg-icons'

const Home = () => {
        const [menuVisibleClass, setMenuVisibleClass] = useState('')
        const menuRef = useRef(null)
        const [graphVisibleClass, setGraphVisibleClass] = useState('')
        const graphRef = useRef(null)
        const [totalAndAvgVisibleClass, setTotalAndAvgVisibleClass] = useState('')
        const totalAndAvgRef = useRef(null)
        const [pointVisibleClass, setPointVisibleClass] = useState('')
        const pointRef = useRef(null)
        const [compareVisibleClass, setCompareVisibleClass] = useState('')
        const compareRef = useRef(null)
        const [categoryVisibleClass, setCategoryVisibleClass] = useState('')
        const categoryRef = useRef(null)
        const [donwloadVisibleClass, setDonwloadVisibleClass] = useState('')
        const downloadRef = useRef(null)

        useEffect(() => {
                const onScroll = () => {
                        const menuTop = menuRef.current.getBoundingClientRect().top;
                        const graphTop = graphRef.current.getBoundingClientRect().top;
                        const totalAndAvgTop = totalAndAvgRef.current.getBoundingClientRect().top;
                        const pointTop = pointRef.current.getBoundingClientRect().top;
                        const compareTop = compareRef.current.getBoundingClientRect().top;
                        const categoryTop = categoryRef.current.getBoundingClientRect().top;
                        const downloadTop = downloadRef.current.getBoundingClientRect().top;
                        const viewportHeight = window.innerHeight;


                        if (menuTop < viewportHeight * 0.9) {
                                setMenuVisibleClass('tutorial-visible');
                        }
                        if (graphTop < viewportHeight * 0.9) {
                                setGraphVisibleClass('tutorial-visible');
                        }
                        if (totalAndAvgTop < viewportHeight * 0.9) {
                                setTotalAndAvgVisibleClass('tutorial-visible');
                        }
                        if (pointTop < viewportHeight * 0.9) {
                                setPointVisibleClass('tutorial-visible');
                        }
                        if (compareTop < viewportHeight * 0.9) {
                                setCompareVisibleClass('tutorial-visible');
                        }
                        if (categoryTop < viewportHeight * 0.9) {
                                setCategoryVisibleClass('tutorial-visible');
                        }
                        if (downloadTop < viewportHeight * 0.9) {
                                setDonwloadVisibleClass('tutorial-visible');
                        }
                };

                // Llama a handleScroll cuando se produce un evento de scroll
                window.addEventListener('scroll', onScroll);

                // Limpia el listener al desmontar el componente
                return () => {
                        window.removeEventListener('scroll', onScroll);
                };
        }, []);

        const openGraph = () => {
                window.open(`/graph/1`, '_self', 'noopener,noreferrer')
        }

        const scrollToTutorial = () => {
                const menuTop = menuRef.current.getBoundingClientRect().top - 120;
                window.scrollTo({
                        top: menuTop,
                        left: 0,
                        behavior: "smooth",
                      })
        }

        return (
                <div className='homepage-container'>
                        <div className='welcome-container'>
                                <div className='welcome-text-container'>
                                        <h1 className='welcome-title'>Descubre que hicieron los grandes <p className='welcome-title-main-words'>Fondos de Inversión</p> con tu acción favorita</h1>
                                        <h3 className='welcome-text'>En FCI Tracker va a poder visualizar el portafolio de los Fondos Comunes de Inversion de Argentina a lo largo del tiempo</h3>
                                        <button onClick={() => openGraph()}>Empezar</button>
                                </div>
                                <img className='welcome-img' src={welcomeImg} alt="" />
                                <FontAwesomeIcon icon={faAngleDown} className='scroll-tutorial'  onClick={scrollToTutorial}/>
                        </div>
                        <div className='tutorial-block tutorial-block-odd'>
                                <div className={`tutorial-text-img-container ${menuVisibleClass}`} ref={menuRef}>
                                        <div className='tutorial-text-img'>
                                                <h2>Con este menu podrás buscar el ticker que desees</h2>
                                                <img className='tutorial-img' src={menuImg} alt="" />
                                        </div>
                                </div>
                        </div>
                        <div className='tutorial-block tutorial-block-even'>
                                <div className={`tutorial-text-img-container ${graphVisibleClass}`} ref={graphRef}>
                                        <div className='tutorial-text-img'>
                                                <img className='tutorial-img' src={graphImg} alt=""/>
                                                <h2>Este es el gráfico de la evolución de tenencia por parte de los fondos en ese activo</h2>
                                        </div>
                                </div>
                        </div>
                        <div className='tutorial-block tutorial-block-odd'>
                                <div className={`tutorial-text-img-container ${totalAndAvgVisibleClass}`} ref={totalAndAvgRef}>
                                        <div className='tutorial-text-img'>
                                                <h2>Tocando el total o el promedio podrás elegir cual quieres que se muestre</h2>
                                                <img className='tutorial-img' src={totalAndAvgImg} alt="" />
                                        </div>
                                </div>
                        </div>
                        <div className='tutorial-block tutorial-block-even'>
                                <div className={`tutorial-text-img-container ${pointVisibleClass}`} ref={pointRef}>
                                        <div className='tutorial-text-img'>
                                                <img className='tutorial-img' src={pointImg} alt="" />
                                                <h2>Tocar cualquier punto te mandará a una página con los detalles del ticker en esa fecha</h2>
                                        </div>
                                </div>
                        </div>
                        <div className='tutorial-block tutorial-block-odd'>
                                <div className={`tutorial-text-img-container ${compareVisibleClass}`} ref={compareRef}>
                                        <div className='tutorial-text-img'>
                                                <h2>Con este menu podrás comparar los datos del ticker en dos fechas distintas</h2>
                                                <img src={compareImg} alt="" />
                                        </div>
                                </div>
                        </div>
                        <div className='tutorial-block tutorial-block-even'>
                                <div className={`tutorial-text-img-container ${categoryVisibleClass}`} ref={categoryRef}>
                                        <div className='tutorial-text-img'>
                                                <img className='tutorial-img' src={categoryImg} alt="" />
                                                <h2>Tocando cualquier categoría podrás ordenar los fondos de manera ascendente o descendente según esa categoría</h2>
                                        </div>
                                </div>
                        </div>
                        <div className='tutorial-block tutorial-block-odd'>
                                <div className={`tutorial-text-img-container ${donwloadVisibleClass}`} ref={downloadRef}>
                                        <div className='tutorial-text-img'>
                                                <h2>Con este botón podrás descargar un excel con los datos que necesites</h2>
                                                <img className='tutorial-img' src={donwloadImg} alt="" />
                                        </div>
                                </div>
                        </div>
                </div>
        )
}

export default Home