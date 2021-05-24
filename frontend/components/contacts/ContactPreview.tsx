import React from "react";

import CustomLink from "../common/CustomLink";
import CustomImage from "../common/CustomImage";
import { usePageDispatch } from "../../lib/context/PageContext";



const ContactPreview = ({ contact }) => {
  const setPage = usePageDispatch();

  const [preview, setPreview] = React.useState(contact);

  if (!contact) return;

  return (
    <div className="contact-preview" style={{margin: 30, padding: "1.5rem 0.5rem" }}>
      <div className="contact-meta">
        <CustomLink
          href="/contacts/[pid]"
          as={`/contacts/${preview.id}`}
        >
          <CustomImage
            src=""
            alt="author's profile image"
          />
        </CustomLink>

        <div className="info">
          <CustomLink
            href="/contacts/[pid]"
            as={`/contacts/${preview.id}`}
            className="author"
          >
            <span style={{color: "#5c78b8"}} onClick={() => setPage(0)}>{preview.name}</span>
          </CustomLink>
        </div>

      </div>

      <CustomLink
        href="/contacts/[pid]"
        as={`/contacts/${preview.id}`}
        className="preview-link"
      >
        <h1>{preview.phoneNumber}</h1>
        <span>Mais detalhes...</span>
      </CustomLink>
    </div>
  );
};

export default ContactPreview;
