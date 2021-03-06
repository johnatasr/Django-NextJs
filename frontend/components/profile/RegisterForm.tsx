import Router from "next/router";
import React from "react";
import { mutate } from "swr";

import ListErrors from "../common/ListErrors";
import UserAPI from "../../lib/api/user";

const RegisterForm = () => {
  const [isLoading, setLoading] = React.useState(false);
  const [errors, setErrors] = React.useState([]);
  const [username, setUsername] = React.useState("");
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [senhaCheck, setSenhaCheck] = React.useState("Senha");

  const handleUsernameChange = React.useCallback(
    (e) => setUsername(e.target.value),
    []
  );
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

    if (password.length < 8) {
      setPassword("")
      setLoading(false)
      setSenhaCheck("Senha deve ser maior que 8 caracteres")
      return {};
    }

    try {
      const { data, status } = await UserAPI.register(
        username,
        email,
        password
      );
      if (status !== 200 && data?.errors) {
        setErrors(data.errors);
      }
      Router.push("/user/login");

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
              placeholder="Usuário"
              value={username}
              onChange={handleUsernameChange}
            />
          </fieldset>

          <fieldset className="form-group">
            <input
              className="form-control form-control-lg"
              type="email"
              placeholder="Email"
              value={email}
              onChange={handleEmailChange}
            />
          </fieldset>

          <fieldset className="form-group">
            <input
              className="form-control form-control-lg"
              type="password"
              placeholder={senhaCheck}
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
            Cadastrar
          </button>
        </fieldset>
      </form>
    </>
  );
};

export default RegisterForm;
