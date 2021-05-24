import Router, { useRouter } from "next/router";
import React from "react";
import useSWR, { trigger } from "swr";

import CustomLink from "../common/CustomLink";
import ContactApi from "../../lib/api/contacts";
import { SERVER_BASE_URL } from "../../lib/utils/constant";
import storage from "../../lib/utils/storage";


const ContactActions = ({ contact }) => {
  const { data: currentUser } = useSWR("user", storage);
  const router = useRouter();
  const {
    query: { pid },
  } = router;

  const handleDelete = async () => {
    const result = window.confirm("Deseja deletar o contato?");

    if (!result) return;

    await ContactApi.delete(pid, currentUser?.tokenAccess);
    trigger(`${SERVER_BASE_URL}/contacts/${pid}/delete`);
    Router.push(`/`, "/", { shallow: false });
  };

  return (
    <>
      <span>
        <CustomLink
          href="/editor/[pid]"
          as={`/editor/${contact.id}`}
          className="btn btn-outline-secondary btn-sm"
        >
          <i className="ion-edit" /> Editar contato
        </CustomLink>

        <button
          className="btn btn-outline-danger btn-sm"
          onClick={handleDelete}
        >
          <i className="ion-trash-a" /> Excluir contato
        </button>
      </span>
    </>
  );
};

export default ContactActions;
