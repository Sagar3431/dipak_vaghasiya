import React from 'react'
import { Link, Outlet } from 'react-router-dom'

function Service() {
  return (
    <div>
      <Link to="/Service/Service1">Service1</Link>{' '} &nbsp;&nbsp;&nbsp;
      <Link to="/Service/Service2">Service2</Link>
      <Outlet></Outlet>
    </div>
  )
}

export default Service
