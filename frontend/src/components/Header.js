import React from "react";
import { Link } from "react-router-dom";
import logo from "../imgs/topbar_logo.png";

const LoggedOutView = () => {
  return (
    <ul className="navbar-nav ml-auto">
      <li className="nav-item">
        <Link to="/login" className="nav-link">
          Sign in
        </Link>
      </li>

      <li className="nav-item">
        <Link to="/register" className="nav-link">
          Sign up
        </Link>
      </li>
    </ul>
  );
};

const LoggedInView = (currentUser) => {
  return (
    <ul className="navbar-nav ml-auto">
      <li className="nav-item">
        <Link to="/editor" className="nav-link">
          <i className="ion-compose"></i>&nbsp;New Item
        </Link>
      </li>

      <li className="nav-item">
        <Link to="/settings" className="nav-link">
          <i className="ion-gear-a"></i>&nbsp;Settings
        </Link>
      </li>

      <li className="nav-item">
        <Link to={`/@${currentUser.username}`} className="nav-link">
          <img
            src={currentUser.image}
            className="user-pic pr-1"
            alt={currentUser.username}
          />
          {currentUser.username}
        </Link>
      </li>
    </ul>
  );
};

function Header({currentUser}) {
  return (
    <nav
      className="navbar navbar-expand-md navbar-dark"
      style={{ padding: "0.5rem 2rem" }}
    >
      <Link to="/" className="navbar-brand">
        <img alt="logo" src={logo} />
      </Link>

      {currentUser ? (
        <LoggedInView currentUser={currentUser} />
      ) : (
        <LoggedOutView />
      )}
    </nav>
  );
}


export default Header;
