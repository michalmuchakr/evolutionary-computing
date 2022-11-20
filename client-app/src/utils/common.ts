import { Dispatch, SetStateAction } from 'react';

export const calculationFormSubmit = (
  setIsModalOpened: Dispatch<SetStateAction<boolean>>,
) => {
  setIsModalOpened(true);
};
