import Vue from 'vue';

const baseUrl = 'http://localhost:5000/api/v1';
const headers = {
  'Content-Type': 'application/json',
};
const authToken = sessionStorage.getItem('addressToken');

export const login = body => Vue.http.post(`${baseUrl}/login`, body, headers);
export const register = body => Vue.http.post(`${baseUrl}/register`, body, headers);
export const validateToken = token => Vue.http.get(`${baseUrl}/validate_token`, {
  headers: {
    ...headers,
    Authorization: `Bearer ${token}`,
  },
});
export const allAddresses = () => Vue.http.get(`${baseUrl}/addresses`, {
  headers: {
    ...headers,
    Authorization: `Bearer ${authToken}`,
  },
});
export const findAddress = id => Vue.http.get(`${baseUrl}/addresses/${id}`, {
  headers: {
    ...headers,
    Authorization: `Bearer ${authToken}`,
  },
});
export const createAddress = body => Vue.http.post(`${baseUrl}/addresses`, body, {
  headers: {
    ...headers,
    Authorization: `Bearer ${authToken}`,
  },
});
export const editAddress = (id, body) => Vue.http.put(`${baseUrl}/addresses/${id}`, body, {
  headers: {
    ...headers,
    Authorization: `Bearer ${authToken}`,
  },
});
export const deleteAddress = id => Vue.http.delete(`${baseUrl}/addresses/${id}`, {
  headers: {
    Authorization: `Bearer ${authToken}`,
  },
});
