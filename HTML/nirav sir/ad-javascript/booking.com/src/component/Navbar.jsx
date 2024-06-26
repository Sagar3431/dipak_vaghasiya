import "./navbar.css"

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="navContainer">
        <span className="logo">Booking.com</span>
        <div className="navItems">
           <button className="nav-INR"><span>INR</span></button>
           <span className="flag"><img src="https://t-cf.bstatic.com/design-assets/assets/v3.94.0/images-flags/In@3x.png" alt=""  /></span>
           <div className="sagar" style={{color:"red"}}><a href="/"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" >
           <path  d="M9.75 9a2.25 2.25 0 1 1 3 2.122 2.25 2.25 0 0 0-1.5 2.122v1.006a.75.75 0 0 0 1.5 0v-1.006c0-.318.2-.602.5-.708A3.75 3.75 0 1 0 8.25 9a.75.75 0 1 0 1.5 0zM12 16.5a1.125 1.125 0 1 0 0 2.25 1.125 1.125 0 0 0 0-2.25.75.75 0 0 0 0 1.5.375.375 0 1 1 0-.75.375.375 0 0 1 0 .75.75.75 0 0 0 0-1.5zM22.5 12c0 5.799-4.701 10.5-10.5 10.5S1.5 17.799 1.5 12 6.201 1.5 12 1.5 22.5 6.201 22.5 12zm1.5 0c0-6.627-5.373-12-12-12S0 5.373 0 12s5.373 12 12 12 12-5.373 12-12z"></path></svg></a></div>
           <a href="/"><span className="e4adce92df">List your property</span></a>
          <button className="navButton">Register</button>
          <button className="navButton">Login</button>
        </div>
        <div className="bar"><i className="fa fa-bars"></i></div>
        
      </div>
    </div>
  )
}

export default Navbar