import * as actionType from './types';

export const setToken = (data) => {
  return {
    type: actionType.SET_TOKEN,
    data
  }
}
// file: src/actions/types.js
export const SET_TOKEN = "SET_TOKEN";