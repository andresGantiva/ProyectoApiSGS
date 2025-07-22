-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 22-07-2025 a las 16:17:56
-- Versión del servidor: 5.7.36
-- Versión de PHP: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_trabajadores_jyb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajadores_tareas`
--

CREATE DATABASE IF NOT EXISTS bd_trabajadores_jyb;
USE bd_trabajadores_jyb;


CREATE TABLE `trabajadores_tareas` (
  `id` int(11) NOT NULL,
  `titulo` varchar(25) NOT NULL,
  `completado` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `trabajadores_tareas`
--

INSERT INTO `trabajadores_tareas` (`id`, `titulo`, `completado`) VALUES
(1, 'Entregar informe', 0),
(13, 'Registrar horas', 0),
(10000, 'Entregar informe', 1),
(10002, 'Registrar nuevo cliente', 1),
(10004, 'Reunion compañeros', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `trabajadores_tareas`
--
ALTER TABLE `trabajadores_tareas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `trabajadores_tareas`
--
ALTER TABLE `trabajadores_tareas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10005;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
