
 import './header.css'

 const Header =()=>{
    return(

        <div className="header">
            <div className="headerContainer">
            <div className="headerList">
                <div className="headerListItem active">
                <i className="fa-solid fa-bed"></i>
                <span>Stays</span>
                </div>

                <div className="headerListItem">
                <i className="fa-solid fa-plane"></i>
                <span>Flight</span>
                </div>

                <div className="headerListItem">
                <i className="fa-solid fa-hotel"></i>
                <span>Flight + Hotel</span>
                </div>

                <div className="headerListItem">
                <i className="fa-solid fa-car"></i>
                <span>Car Rentals</span>
                </div>

                <div className="headerListItem">
                <i className="fa-solid fa-magnet"></i>
                <span>Attractions</span>
                </div>

                <div className="headerListItem">
                <i className="fa-solid fa-taxi"></i>
                <span>Airport Texis</span>
                </div>
            </div>
            </div>
        </div>
    )
 }

 export default Header