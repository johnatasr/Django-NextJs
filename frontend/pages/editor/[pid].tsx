import axios from "axios";
import Router, { useRouter } from "next/router";
import React, { useState } from "react";
import useSWR from "swr";

import ListErrors from "../../components/common/ListErrors";
import ContactsApi from "../../lib/api/contacts";
import { SERVER_BASE_URL } from "../../lib/utils/constant";
import editorReducer from "../../lib/utils/editorReducer";
import storage from "../../lib/utils/storage";

const UpdateContactEditor = ({ contact: initialContact }) => {
  const initialState = {
    id: initialContact.id,
    name: initialContact.name,
    phoneNumber: initialContact.phoneNumber,
  };

  const [isLoading, setLoading] = React.useState(false);
  const [errors, setErrors] = React.useState([]);
  const [contactPosting, dispatch] = React.useReducer(editorReducer, initialState);
  const { data: currentUser } = useSWR("user", storage);
  const router = useRouter();
  const [name, setName] = useState();
  const [phoneNumber, setPhoneNumber] = useState();

  const {
    query: { pid },
  } = router;

  const handleName = (e) =>
    dispatch({ name: e.target.value });
  const handlePhoneNumber = (e) =>
    dispatch({ phoneNumber: e.target.value });


  function tex(){
    console.log(contactPosting)
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const { data, status } = await axios.put(
      `${SERVER_BASE_URL}/contacts/${pid}/update`,
      JSON.stringify({ name: contactPosting.name, phoneNumber: contactPosting.phoneNumber }),
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `JWT ${currentUser?.token}`,
        },
      }
    );
    setLoading(false);

    if (status !== 200) {
      setErrors(data.errors);
    }

    Router.push(`/`);
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
                    value={contactPosting.name}
                    onChange={handleName}
                  />
                </fieldset>

                <fieldset className="form-group">
                  <input
                    className="form-control form-control-lg"
                    type="text"
                    placeholder="Qual o número de telefone ?"
                    value={contactPosting.phoneNumber}
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
                  Atualizar contato
                </button>
              </fieldset>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

UpdateContactEditor.getInitialProps = async ({ query: { pid } }) => {
  const {
    data: { contact },
  } = await ContactsApi.get(pid);
  return { contact };
};

export default UpdateContactEditor;
