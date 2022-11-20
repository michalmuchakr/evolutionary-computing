import { Modal, ModalHeader, ModalBody } from 'reactstrap';

const ResultModal = ({
  isModalOpened,
  hideModal,
  response
}: {
  isModalOpened: boolean;
  hideModal: () => void;
  response: {
    x1: string,
    x2: string,
    fitFunVal: string
  } | null;
}) => {
  return (
    <Modal isOpen={isModalOpened}>
      <ModalHeader toggle={hideModal}>Result modal</ModalHeader>
      <ModalBody>
        {response && (
          `f(${response.x1}, ${response.x2}) = ${response.fitFunVal}`
        )}
      </ModalBody>
    </Modal>
  );
};

export default ResultModal;
