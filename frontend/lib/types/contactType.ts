export interface ContactsList {
    contacts: ContactType[];
}
  
export interface Contact {
    contact: ContactType;
}

export type ContactType = {
    id: number;
    userId: number;
    name: string;
    phoneNumber: string;
};
  

  