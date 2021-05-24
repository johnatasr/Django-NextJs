import Router from "next/router";
import React, { useState } from "react";
import useSWR from "swr";

import ListErrors from "../../components/common/ListErrors";
import ContactsApi from "../../lib/api/contacts";
import storage from "../../lib/utils/storage";
import editorReducer from "../../lib/utils/editorReducer";


const PublishContactEditor = () => {
  const initialState = {
    name: "",
    phoneNumber: "",
  };

  const [isLoading, setLoading] = React.useState(false);
  const [errors, setErrors] = React.useState([]);
  const [posting, dispatch] = React.useReducer(editorReducer, initialState);
  const { data: currentUser } = useSWR("user", storage);
  const [ name, setName ] = useState();
  const [ phoneNumber, setPhoneNumber ] = useState()
  const [ alert, setAlert ] = useState("");


  const handleName = (e) =>
    setName(e.target.value);
  const handlePhoneNumber = (e) =>
    setPhoneNumber(e.target.value);
 
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    if ((name == undefined || name == "") && (phoneNumber == undefined || phoneNumber == "")) {
      setAlert("Todos os campos devem ser preenchidos")
      return {}
    }

    const { data, status } = await ContactsApi.create(
      posting,
      currentUser?.token
    );

    setLoading(false);

    if (status !== 200) {
      setErrors(data.errors);
    }

    Router.push("/");
  };

  return (
    <div className="editor-page">
      <div className="container page">
        <div className="row">
          <div className="col-md-10 offset-md-1 col-xs-12">
            <ListErrors errors={errors} />
            <form>
              <fieldset>
                <fieldset className="form-group">
                  <input
                    className="form-control form-control-lg"
                    type="text"
                    placeholder="Nome do contato"
                    value={name}
                    onChange={handleName}
                  />
                </fieldset>

                <fieldset className="form-group">
                  <input
                    className="form-control form-control-lg"
                    type="text"
                  placeholder="Adicione o número. Ex: (85) 9999-9999"
                    value={phoneNumber}
                    onChange={handlePhoneNumber}
                  />
                </fieldset>
           
                <button
                  className="btn btn-lg pull-xs-right btn-primary"
                  type="button"
                  disabled={isLoading}
                  onClick={handleSubmit}
                  style={{background: "#5c78b8"}}
                >
                  Adicionar contato
                </button>
              </fieldset>
            </form>
          </div>
        </div>
        <div className="row">
          <div className="col-md-10 offset-md-1 col-xs-12" style={{color: "red"}}>
            <h5>{alert}</h5>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PublishContactEditor;
