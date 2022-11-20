import { Dispatch, SetStateAction } from 'react';

export const calculationFormSubmit = (
  setIsModalOpened: Dispatch<SetStateAction<boolean>>,
) => {
  console.log('hello calculationFormSubmit');
  setIsModalOpened(true);
};
