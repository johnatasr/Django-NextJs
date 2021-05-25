import Router from "next/router";
import React from "react";
import useSWR, { mutate, trigger } from "swr";

import SettingsForm from "../../components/profile/SettingsForm";
import checkLogin from "../../lib/utils/checkLogin";
import storage from "../../lib/utils/storage";
import { logoutCookie } from "lib/utils/authCookies"

const Settings = ({ res }) => {
  const { data: currentUser } = useSWR("user", storage);
  const isLoggedIn = checkLogin(currentUser);

  if (!isLoggedIn) {
    if (res) {
      res.writeHead(302, {
        Location: "/user/login",
      });
      res.end();
    }
    Router.push(`/user/login`);
  }

  const handleLogout = async (e) => {
    e.preventDefault();
    window.localStorage.removeItem("user");
    logoutCookie()
    mutate("user", null);
    Router.push(`/user/login`).then(() => trigger("user"));
  };

  return (
    <div className="settings-page">
      <div className="container page">
        <div className="row">
          <div className="col-md-6 offset-md-3 col-xs-12">
            <h1 className="text-xs-center">Suas configurações</h1>
            <SettingsForm />
            <hr />
            <button className="btn btn-outline-danger" onClick={handleLogout}>
              Ou clique aqui para logout.
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

Settings.getInitialProps = async ({ res }) => {
  return {
    res,
  };
};

export default Settings;
