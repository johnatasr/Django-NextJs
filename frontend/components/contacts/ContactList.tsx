import styled from "@emotion/styled";
import { useRouter } from "next/router";
import Router from "next/router";
import React, { useMemo, useEffect, useState } from "react";

import ContactPreview from "components/contacts/ContactPreview";
import ErrorMessage from "components/common/ErrorMessage";
import LoadingSpinner from "components/common/LoadingSpinner";
import ContactsApi from "lib/api/contacts";
import { usePageState } from "lib/context/PageContext";
import {
  usePageCountState,
  usePageCountDispatch,
} from "lib/context/PageCountContext";
import { getToken } from "lib/utils/authToken"

const EmptyMessage = styled("div")`
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  padding: 1.5rem 0;
`;


const ContactList = () => {
  const page = usePageState();
  const pageCount = usePageCountState();
  const setPageCount = usePageCountDispatch();
  const lastIndex =
    pageCount > 480 ? Math.ceil(pageCount / 20) : Math.ceil(pageCount / 20) - 1;

  const router = useRouter();
  const { asPath, pathname, query } = router;
  const { pid } = query;
  const [ contacts, setContacts ] = useState([])
  const [ countContacts, setCountContacts ] = useState()
  const [ status, setStatus ] = useState()

  useEffect(() => {
    async function getContacts() {
      const token = getToken();

      // if (!token) {
      //   Router.push('/user/login') 
      //   return {} 
      // };

      const response = await ContactsApi.all(token)

      if (!response.data) return setContacts([])

      const { contacts, contactsCount } = response.data;
      setStatus(response.status)
      setCountContacts(contactsCount)
      setContacts(contacts)

      return contacts
    }
    getContacts();
  }, [])

  if (status === 401)   Router.push('/user/login');

  if (status !== 200) return <ErrorMessage message="Não foi possível carregar os contatos..." />;
  
  if (!contacts) return <LoadingSpinner />;

  if (contacts?.length === 0) {
    return <EmptyMessage>Nenhum contato encontrado...</EmptyMessage>;
  }

  return (
    <>
      {contacts?.map((contact) => (
        <ContactPreview key={contact.id} contact={contact} />
      ))}

    </>
  );
};

export default ContactList;
