import Vue from 'vue';

const baseUrl = 'http://localhost:5000/api/v1';

export const login = body => Vue.http.post(`${baseUrl}/login`, body, {
  headers: { 'Content-Type': 'application/json' },
});

export const register = body => Vue.http.post(`${baseUrl}/register`, body, {
  headers: { 'Content-Type': 'application/json' },
});

export const validateToken = token => Vue.http.get(`${baseUrl}/validate_token`, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`,
  },
});

export const allAddresses = () => Vue.http.get(`${baseUrl}/addresses`, {
  headers: {
    Authorization: `Bearer ${sessionStorage.getItem('addressToken')}`,
  },
});

export const findAddress = id => Vue.http.get(`${baseUrl}/addresses/${id}`, {
  headers: {
    Authorization: `Bearer ${sessionStorage.getItem('addressToken')}`,
  },
});

export const createAddress = body => Vue.http.post(`${baseUrl}/addresses`, body, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${sessionStorage.getItem('addressToken')}`,
  },
});

export const editAddress = (id, body) => Vue.http.put(`${baseUrl}/addresses/${id}`, body, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${sessionStorage.getItem('addressToken')}`,
  },
});

export const deleteAddress = id => Vue.http.delete(`${baseUrl}/addresses/${id}`, {
  headers: {
    Authorization: `Bearer ${sessionStorage.getItem('addressToken')}`,
  },
});
