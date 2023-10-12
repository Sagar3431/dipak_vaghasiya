import React from 'react'
import "./center.css"
import img1 from './img/img1.jpg'
import img2 from './img/img2.jpg'
import img3 from './img/img3.jpg'
import img4 from './img/img4.webp'

export default function Center() {
  return (
    <div className="content">
        <div className="results">
          <li><a href="#">Home</a></li>
          <li><i className="fa-solid fa-angle-right"></i></li>
          <li><a href="#">India</a></li>
          <li><i className="fa-solid fa-angle-right"></i></li>
          <li><a href="#">Goa</a></li>
          <li><i className="fa-solid fa-angle-right"></i></li>
          <li>Search results</li>
        </div>
        <div className="properties">
          <div className="map">
          </div>
          <div className="trip">
            <h4>Goa: 1,907 properties found</h4>
            <p>Get inspiration for your next trip</p>
            <div className="beaches">
              <li className="active"><a href="#"><i className="fa-solid fa-umbrella-beach"></i> Beaches</a></li>
              <li><a href="#"><i className="fa-solid fa-heart-pulse"></i> Romantic</a></li>
              <li><a href="#"><i className="fa-solid fa-people-roof"></i> Family-Friendly</a></li>
              <li><a href="#"><i className="fa-solid fa-moon"></i> Nightlife</a></li>
            </div>
            <div className="sliding">
              <div className="sliding1">
                <img src={img1} alt="" height="90%" width="40%"/>
                <div className="write">
                <h5>Agonda</h5>
                <p>Relax in nature .beaches .Family-friendly</p>
                </div>
              </div>
              <div className="sliding1">
                <img src={img2} alt="" height="90%" width="40%" />
                <div className="write">
                <h5>Arambol</h5>
                <p>Relax in nature .beaches .Family-friendly</p>
                </div>
              </div>
              <div className="sliding1">
              <img src={img3} alt="" height="90%" width="40%" />
              <div className="write">
                <h5>Benaulim</h5>
                <p>Relax in nature .beaches .Family-friendly</p>
                </div>
              </div>
            </div>
              <div className="hotel5">
              
              <div className="hotels">
                <div className="hotel_photo">
                  <img src={img4} alt="" height="100%" width="100%"/>
                  <span><i className="fa-regular fa-heart"></i></span>
                </div>
                <div className="hotel_details">
                  <div className="hotel_name">
                    <div className="hotel_title"><a href="#">Hotel Halcyon, Near Candolim Beach</a><span><i className="fa-solid fa-star"></i><i className="fa-solid fa-star"></i></span></div>
                    <div className="hotel_review"><span>Good</span> 6reviews</div>
                    <div className="hotel_rating">7.2</div>
                  </div>
                  <div className="places_nearby"><a href="#"><span>Candolim Beach, Candolim</span> <span>Show on map</span></a></div>
                  <button><a href="#">Limited-time deal</a></button>
                  <div className="room_type">
                    <div className="room_details">
                      <p>Deluxe Double Room</p>
                      <p>1 queen bed</p>
                      <p>Only 3 rooms left at this price on our site</p>
                    </div>
                    <div className="room_price">
                      <p>1night, 2adults</p>
                      <p><span>$3182 </span>$1909</p>
                      <p>+$229 taxes and charges</p>
                      <button className="available"><a href="#">See availability <i className="fa-solid fa-angle-right"></i></a></button>
                    </div>
                  </div>
                </div>
                </div>

                <div className="hotels">
                <div className="hotel_photo">
                  <img src={img4} alt="" height="100%" width="100%"/>
                  <span><i className="fa-regular fa-heart"></i></span>
                </div>
                <div className="hotel_details">
                  <div className="hotel_name">
                    <div className="hotel_title"><a href="#">Hotel Halcyon, Near Candolim Beach</a><span><i className="fa-solid fa-star"></i><i className="fa-solid fa-star"></i></span></div>
                    <div className="hotel_review"><span>Good</span> 6reviews</div>
                    <div className="hotel_rating">7.2</div>
                  </div>
                  <div className="places_nearby"><a href="#"><span>Candolim Beach, Candolim</span> <span>Show on map</span></a></div>
                  <button><a href="#">Limited-time deal</a></button>
                  <div className="room_type">
                    <div className="room_details">
                      <p>Deluxe Double Room</p>
                      <p>1 queen bed</p>
                      <p>Only 3 rooms left at this price on our site</p>
                    </div>
                    <div className="room_price">
                      <p>1night, 2adults</p>
                      <p><span>$3182 </span>$1909</p>
                      <p>+$229 taxes and charges</p>
                      <button className="available"><a href="#">See availability <i className="fa-solid fa-angle-right"></i></a></button>
                    </div>
                  </div>
                </div>
                </div>

                 
                <div className="hotels">
                <div className="hotel_photo">
                  <img src={img4} alt="" height="100%" width="100%"/>
                  <span><i className="fa-regular fa-heart"></i></span>
                </div>
                <div className="hotel_details">
                  <div className="hotel_name">
                    <div className="hotel_title"><a href="#">Hotel Halcyon, Near Candolim Beach</a><span><i className="fa-solid fa-star"></i><i className="fa-solid fa-star"></i></span></div>
                    <div className="hotel_review"><span>Good</span> 6reviews</div>
                    <div className="hotel_rating">7.2</div>
                  </div>
                  <div className="places_nearby"><a href="#"><span>Candolim Beach, Candolim</span> <span>Show on map</span></a></div>
                  <button><a href="#">Limited-time deal</a></button>
                  <div className="room_type">
                    <div className="room_details">
                      <p>Deluxe Double Room</p>
                      <p>1 queen bed</p>
                      <p>Only 3 rooms left at this price on our site</p>
                    </div>
                    <div className="room_price">
                      <p>1night, 2adults</p>
                      <p><span>$3182 </span>$1909</p>
                      <p>+$229 taxes and charges</p>
                      <button className="available"><a href="#">See availability <i className="fa-solid fa-angle-right"></i></a></button>
                    </div>
                  </div>
                </div>
                </div>

                
                <div className="hotels">
                <div className="hotel_photo">
                  <img src={img4} alt="" height="100%" width="100%"/>
                  <span><i className="fa-regular fa-heart"></i></span>
                </div>
                <div className="hotel_details">
                  <div className="hotel_name">
                    <div className="hotel_title"><a href="#">Hotel Halcyon, Near Candolim Beach</a><span><i className="fa-solid fa-star"></i><i className="fa-solid fa-star"></i></span></div>
                    <div className="hotel_review"><span>Good</span> 6reviews</div>
                    <div className="hotel_rating">7.2</div>
                  </div>
                  <div className="places_nearby"><a href="#"><span>Candolim Beach, Candolim</span> <span>Show on map</span></a></div>
                  <button><a href="#">Limited-time deal</a></button>
                  <div className="room_type">
                    <div className="room_details">
                      <p>Deluxe Double Room</p>
                      <p>1 queen bed</p>
                      <p>Only 3 rooms left at this price on our site</p>
                    </div>
                    <div className="room_price">
                      <p>1night, 2adults</p>
                      <p><span>$3182 </span>$1909</p>
                      <p>+$229 taxes and charges</p>
                      <button className="available"><a href="#">See availability <i className="fa-solid fa-angle-right"></i></a></button>
                    </div>
                  </div>
                </div>
                </div>
                


                <div className="hotels">
                <div className="hotel_photo">
                  <img src={img4} alt="" height="100%" width="100%"/>
                  <span><i className="fa-regular fa-heart"></i></span>
                </div>
                <div className="hotel_details">
                  <div className="hotel_name">
                    <div className="hotel_title"><a href="#">Hotel Halcyon, Near Candolim Beach</a><span><i className="fa-solid fa-star"></i><i className="fa-solid fa-star"></i></span></div>
                    <div className="hotel_review"><span>Good</span> 6reviews</div>
                    <div className="hotel_rating">7.2</div>
                  </div>
                  <div className="places_nearby"><a href="#"><span>Candolim Beach, Candolim</span> <span>Show on map</span></a></div>
                  <button><a href="#">Limited-time deal</a></button>
                  <div className="room_type">
                    <div className="room_details">
                      <p>Deluxe Double Room</p>
                      <p>1 queen bed</p>
                      <p>Only 3 rooms left at this price on our site</p>
                    </div>
                    <div className="room_price">
                      <p>1night, 2adults</p>
                      <p><span>$3182 </span>$1909</p>
                      <p>+$229 taxes and charges</p>
                      <button className="available"><a href="#">See availability <i className="fa-solid fa-angle-right"></i></a></button>
                    </div>
                  </div>
                </div>
                </div>
                

                <div className="hotels">
                <div className="hotel_photo">
                  <img src={img4} alt="" height="100%" width="100%"/>
                  <span><i className="fa-regular fa-heart"></i></span>
                </div>
                <div className="hotel_details">
                  <div className="hotel_name">
                    <div className="hotel_title"><a href="#">Hotel Halcyon, Near Candolim Beach</a><span><i className="fa-solid fa-star"></i><i className="fa-solid fa-star"></i></span></div>
                    <div className="hotel_review"><span>Good</span> 6reviews</div>
                    <div className="hotel_rating">7.2</div>
                  </div>
                  <div className="places_nearby"><a href="#"><span>Candolim Beach, Candolim</span> <span>Show on map</span></a></div>
                  <button><a href="#">Limited-time deal</a></button>
                  <div className="room_type">
                    <div className="room_details">
                      <p>Deluxe Double Room</p>
                      <p>1 queen bed</p>
                      <p>Only 3 rooms left at this price on our site</p>
                    </div>
                    <div className="room_price">
                      <p>1night, 2adults</p>
                      <p><span>$3182 </span>$1909</p>
                      <p>+$229 taxes and charges</p>
                      <button className="available"><a href="#">See availability <i className="fa-solid fa-angle-right"></i></a></button>
                    </div>
                  </div>
                </div>
                </div>


              </div>
          </div>
        </div>
      </div>
  )
}
