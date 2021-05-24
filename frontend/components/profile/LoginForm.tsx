import Router from "next/router";
import React from "react";
import { mutate } from "swr";

import ListErrors from "../common/ListErrors";
import UserAPI from "../../lib/api/user";

const LoginForm = () => {
  const [isLoading, setLoading] = React.useState(false);
  const [errors, setErrors] = React.useState([]);
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");

  const handleEmailChange = React.useCallback(
    (e) => setEmail(e.target.value),
    []
  );
  const handlePasswordChange = React.useCallback(
    (e) => setPassword(e.target.value),
    []
  );

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const { data, status } = await UserAPI.login(email, password);

      if (status !== 200) {
        setErrors(data.errors);
      }

      if (data) {
        window.localStorage.setItem("user", JSON.stringify({ tokenAccess: data.access, refreshToken: data.refresh, username: data.username }));
        mutate("user", data?.user);
        Router.push("/");
      }
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <ListErrors errors={errors} />

      <form onSubmit={handleSubmit}>
        <fieldset>
          <fieldset className="form-group">
            <input
              className="form-control form-control-lg"
              type="text"
              placeholder="Entre com seu usuário"
              value={email}
              onChange={handleEmailChange}
            />
          </fieldset>

          <fieldset className="form-group">
            <input
              className="form-control form-control-lg"
              type="password"
              placeholder="Digite sua senha"
              value={password}
              onChange={handlePasswordChange}
            />
          </fieldset>

          <button
            className="btn btn-lg btn-primary pull-xs-right"
            type="submit"
            disabled={isLoading}
            style={{background: "#5c78b8"}}
          >
            Entre
          </button>
        </fieldset>
      </form>
    </>
  );
};

export default LoginForm;
