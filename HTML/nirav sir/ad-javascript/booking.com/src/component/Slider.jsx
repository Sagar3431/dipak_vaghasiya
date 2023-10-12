import './slider.css'


const Slider =()=>{
   return(

       <div className="slider">
         <div className="main">
                    <div className="headerSearch">
                            <div className="main1">
                               <div className="headerSearchItem">
                                  <i className="fa fa-bed headerIcon"></i>
                                  <input type="text" placeholder="Where are you going" className="headerSearchInput"/>
                               </div>
                            </div>
                     
                            <div className="main1">
                               <div className="headerSearchItem">
                                    <i className="fa-regular fa-calendar-days headerIcon"></i>
                                    <span className="headerSearchText">Cheak-in date - Cheak-out date</span>
                               </div>
                            </div>
                        
                            <div className="main1">
                              <div className="headerSearchItem">
                                    <i className="fa fa-user headerIcon"></i>
                                    <span className="headerSearchText">2 Adults . 0 children .1 room</span>
                              </div>
                            </div>
                      
                             <div className="main2">
                               <div className="headerSearchItem">
                                 <button className="headerBtn1">Search</button>
                               </div>
                             </div>
                    </div>
             </div>
                             <div className="sliderImg">
                                 <div className="text">
                                    <h1>Howzat for a perfect stay</h1>
                                    <p>Search hotels, homes and much more</p>
                                    <button className='btn2'>Discover More</button>
                                 </div>
                             </div>
       </div>
   )
}

export default Slider