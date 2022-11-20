import {Modal, ModalHeader, ModalBody, CardText, Alert} from 'reactstrap';

const ResultModal = ({
                       isLoading,
                       isModalOpened,
                       hideModal,
                       response,
                       backendError,
                     }: {
  isLoading: boolean;
  isModalOpened: boolean;
  hideModal: () => void;
  response: {
    executionTime: string;
    x1: string,
    x2: string,
    fitFunVal: string,
  } | null;
  backendError: any;
}) => {
  return (
    <Modal isOpen={isModalOpened && !isLoading && !backendError} size="lg" backdrop={true} toggle={hideModal}>
      <ModalHeader toggle={hideModal}>Result modal</ModalHeader>
      <ModalBody>
        {response && !backendError && (
          <>
            <CardText>
              {`f( ${response.x1}, ${response.x2} ) = ${response.fitFunVal}`}
            </CardText>
            <CardText>
              {`execution time: ${response.executionTime} s`}
            </CardText>
          </>
        )}
        {backendError && (
          <Alert color="danger">
            {backendError}
          </Alert>
        )}
      </ModalBody>
    </Modal>
  );
};

export default ResultModal;
