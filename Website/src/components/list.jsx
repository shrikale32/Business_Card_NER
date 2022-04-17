import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import CRUDTable,
{
  Fields,
  Field,
  CreateForm,
  UpdateForm,
  DeleteForm,
} from 'react-crud-table';

import "../styles/list.css"

const serverUrl = "http://127.0.0.1:8000";

const DescriptionRenderer = ({ field }) => <textarea {...field} />;

let cards = [
  {
    id: 1,
    name: 'Hitesh Dharmadhikari',
    phone: '+1 4372404645',
    email: 'hdharma1@my.centennialcollege.ca',
    website: 'www.hieetesh.com',
    address: '10 Eaglewing CT, Scaroborough, ON'
  },
  {
    id: 2,
    name: 'Shrikant Kale',
    phone: '+1 4372402324',
    email: 'skale5@my.centennialcollege.ca',
    website: 'www.wap.com',
    address: '10 Eaglewing CT, Scaroborough, ON'
  },
];

const SORTERS = {
  NUMBER_ASCENDING: mapper => (a, b) => mapper(a) - mapper(b),
  NUMBER_DESCENDING: mapper => (a, b) => mapper(b) - mapper(a),
  STRING_ASCENDING: mapper => (a, b) => mapper(a).localeCompare(mapper(b)),
  STRING_DESCENDING: mapper => (a, b) => mapper(b).localeCompare(mapper(a)),
};

const getSorter = (data) => {
  const mapper = x => x[data.field];
  let sorter = SORTERS.STRING_ASCENDING(mapper);

  if (data.field === 'id') {
    sorter = data.direction === 'ascending' ?
      SORTERS.NUMBER_ASCENDING(mapper) : SORTERS.NUMBER_DESCENDING(mapper);
  } else {
    sorter = data.direction === 'ascending' ?
      SORTERS.STRING_ASCENDING(mapper) : SORTERS.STRING_DESCENDING(mapper);
  }

  return sorter;
};

let count = cards.length;
const service = {
  fetchItems: (payload) => {

    let result = Array.from(cards);
    result = result.sort(getSorter(payload.sort));
    return Promise.resolve(result);
  },
  create: (card) => {
    count += 1;
    cards.push({
      ...card,
      id: count,
    });
    return Promise.resolve(card);
  },
  update: (data) => {
    const card = cards.find(t => t.id === data.id);
    card.title = data.title;
    card.description = data.description;
    return Promise.resolve(card);
  },
  delete: (data) => {
    const card = cards.find(t => t.id === data.id);
    cards = cards.filter(t => t.id !== card.id);
    return Promise.resolve(card);
  },
};

const styles = {
    container: { margin: 'auto', width: 'fit-content' },
  };

function List(props) {

    useEffect(()=>{
      let user_id = localStorage.getItem('user_sub');
      fetch(serverUrl + "/card/"+user_id, {
        method: "GET",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
      }).then(response => response.json())
      .then(res=>{
        console.log("res666", res)
      })
      .catch((error)=>{
          console.log(error)
      })
    },[])

    return (
        <div>
          <div style={styles.container}>
            <CRUDTable
              caption="Cards"
              fetchItems={payload => service.fetchItems(payload)}
            >
              <Fields>
                <Field
                  name="id"
                  label="Id"
                  hideInCreateForm
                  readOnly
                />
                <Field
                  name="name"
                  label="Name"
                />
                <Field
                  name="phone"
                  label="Phone"
                />
                <Field
                  name="email"
                  label="Email"
                />
                <Field
                  name="website"
                  label="Website"
                />
                <Field
                  name="address"
                  label="address"
                  render={DescriptionRenderer}
                />
              </Fields>
              <CreateForm
                title="Card Creation"
                message="Create a new card!"
                trigger="Create Card"
                onSubmit={task => service.create(task)}
                submitText="Create"
                validate={(values) => {
                  const errors = {};
                  if (!values.title) {
                    errors.title = 'Please, provide card\'s title';
                  }

                  if (!values.description) {
                    errors.description = 'Please, provide card\'s description';
                  }

                  return errors;
                }}
              />

              <UpdateForm
                title="Card Update Process"
                message="Update task"
                trigger="Update"
                onSubmit={task => service.update(task)}
                submitText="Update"
                validate={(values) => {
                  const errors = {};

                  if (!values.id) {
                    errors.id = 'Please, provide id';
                  }

                  if (!values.title) {
                    errors.title = 'Please, provide task\'s title';
                  }

                  if (!values.description) {
                    errors.description = 'Please, provide task\'s description';
                  }

                  return errors;
                }}
              />

              <DeleteForm
                title="Card Delete Process"
                message="Are you sure you want to delete the task?"
                trigger="Delete"
                onSubmit={task => service.delete(task)}
                submitText="Delete"
                validate={(values) => {
                  const errors = {};
                  if (!values.id) {
                    errors.id = 'Please, provide id';
                  }
                  return errors;
                }}
              />
            </CRUDTable>
          </div>
        </div>
    );
}

export default List;