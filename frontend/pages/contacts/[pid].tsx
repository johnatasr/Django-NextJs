import styled from "@emotion/styled";
import React, { useEffect, useState } from "react";

import LoadingSpinner from "components/common/LoadingSpinner";
import ContactAction from "components/contacts/ContactActions";
import ContactsApi from "lib/api/contacts";
import { ContactType } from "lib/types/contactType";

interface ContactPageProps {
  contact: ContactType;
  pid: string;
}

const ContactPageContainer = styled("div")``;

const ContactInfoContainer = styled("div")`
  color: #fff;
  background: #333;
  margin-bottom: 2rem;
  padding: 2rem 0;
`;

const ContactInfoPresenter = styled("div")`
  margin: 0 auto;
  padding: 0 15px;

  @media (min-width: 544px) {
    max-width: 576px;
  }

  @media (min-width: 768px) {
    max-width: 720px;
  }

  @media (min-width: 992px) {
    max-width: 940px;
  }

  @media (min-width: 1200px) {
    max-width: 1140px;
  }
`;

const ContactTitle = styled("h1")`
  margin: 0;
  font-size: 2.8rem;
  font-weight: 600;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  line-height: 1.1;
`;

const ContactContentContainer = styled("div")`
  margin: 1.5rem auto 0;
  padding: 0 15px;

  @media (min-width: 544px) {
    max-width: 576px;
  }

  @media (min-width: 768px) {
    max-width: 720px;
  }

  @media (min-width: 992px) {
    max-width: 940px;
  }

  @media (min-width: 1200px) {
    max-width: 1140px;
  }
`;

const ContactContentPresenter = styled("div")`
  position: relative;
  display: flex;
  flex-wrap: wrap;
  flex: 0 0 100%;
  max-width: 100%;
  min-height: 1px;
  margin: 0 -15px;
  padding: 0 15px;
`;

const Divider = styled("hr")`
  box-sizing: content-box;
  height: 0;
  margin-top: 1rem;
  margin-bottom: 1rem;
  border: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
`;


const ContactPage = ({ pid }: ContactPageProps) => {
  
  const [ contact, setContact ] = useState();


  useEffect(() => {
    async function getContact() {
      const response = await ContactsApi.get(pid)
      const { contact } = response.data;

      setContact(contact)

      return contact
    }
    getContact();
  }, [contact])

  if (!contact) return <LoadingSpinner />;

  return (
    <ContactPageContainer>
      <ContactInfoContainer>
        <ContactInfoPresenter>
          <ContactTitle> {contact.phoneNumber} </ContactTitle>
          <h2> {contact.name} </h2>
        </ContactInfoPresenter>
      </ContactInfoContainer>
      <ContactContentContainer>
        <ContactContentPresenter className="contact-content">
        </ContactContentPresenter>
        <Divider />
        <ContactAction contact={contact} />
      </ContactContentContainer>
    </ContactPageContainer>
  );
};

export async function getStaticPaths() {
  return { paths: [], fallback: true };
}

export async function getStaticProps({ params }) {
  const { pid } = params;

  try {
    return {
      props: {
        pid,
      },
      revalidate: 1,
    };
  } catch (error) {
    console.error(`Get contact id ${pid} error: `, error);
    return {
      props: {
        article: {},
        pid,
      },
      revalidate: 1,
    };
  }
}

export default ContactPage;
