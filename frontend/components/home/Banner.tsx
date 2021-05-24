import React from "react";

import { APP_NAME } from "../../lib/utils/constant";

const Banner = () => (
  <div className="banner" style={{background: "#5c78b8"}}>
    <div className="container">
      <h1 className="logo-font">{APP_NAME.toLowerCase()}</h1>
      <p>Uma lista de contatos muito TOP.</p>
    </div>
  </div>
);

export default Banner;
