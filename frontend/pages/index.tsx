import styled from "@emotion/styled";
import Router from "next/router";
import Head from "next/head";
import React, { useEffect } from "react";

import ContactList from "components/contacts/ContactList";
import Banner from "components/home/Banner";


const IndexPageContainer = styled("div")``;

const IndexPagePresenter = styled("div")`
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

const MainContent = styled("div")`
  display: flex;
  flex-wrap: wrap;
  margin-left: -15px;
  margin-right: -15px;
`;

const ContentContainer = styled("div")`
  width: 100%;
  @media (min-width: 768px) {
    position: relative;
    min-height: 1px;
    padding-right: 15px;
    padding-left: 15px;
    flex: 0 0 75%;
    max-width: 75%;
  }
`;

const IndexPage = () => {
  useEffect(() => {
    const userAuth = localStorage.getItem("user");

    if (!userAuth) {
      Router.push('/user/login');
    }
  }, []);

  return (
    <>
      <Head>
        <title>HOME | ContactList</title>
        <meta
          name="description"
          content="Projeto de lista de contatos"
        />
      </Head>
      <IndexPageContainer className="home-page">
        <Banner />
        <IndexPagePresenter>
          <MainContent>
            <ContentContainer style={{margin: 80}}>
              <ContactList />
            </ContentContainer>
          </MainContent>
        </IndexPagePresenter>
      </IndexPageContainer>
    </>
  ) 
};

export default IndexPage;
