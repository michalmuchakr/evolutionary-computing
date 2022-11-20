import { FormEvent, useState } from 'react';
import { Col, Container, Row } from 'reactstrap';
import InitialCalculationDataForm from './components/InitialCalculationDataForm';
import ResultModal from './components/ResultModal';
import { calculationFormSubmit } from './utils/common';
import axios from "axios";

const App = () => {
  const [beginOfrRange, setBeginOfRange] = useState('');
  const [endOfRange, setEndOfRange] = useState('');
  const [populationMembersCount, setPopulationMembersCount] = useState('');
  const [epochsCount, setEpochsCount] = useState('');
  const [chromosomCount, setChromosomCount] = useState('');
  const [eliteStrategyCount, setEliteStrategyCount] = useState('');
  const [bitsCount, setBitsCount] = useState('');
  const [crossProbablility, setCrossProbablility] = useState('');
  const [mutationProbability, setMutationProbability] = useState('');
  const [inversionProbability, setInversionProbability] = useState('');
  const [selectionMethod, setSelectionMethod] = useState('best');
  const [crossMethod, setCrossMethod] = useState('one_point');
  const [mutationMethod, setMutationMethod] = useState('one_point');

  const [isModalOpened, setIsModalOpened] = useState(false);

  const [response, setResponse] = useState<{
    x1: string,
    x2: string,
    fitFunVal: string
  } | null>(null);

  const hideModal = () => {
    setIsModalOpened(false);
  };

  const onFormSubmit = (e: FormEvent) => {
    e.preventDefault();

    axios.post('http://127.0.0.1:8000/eo/', {
      begin_of_range: beginOfrRange,
      end_of_range: endOfRange,
      population_members_count: populationMembersCount,
      chromosom_count: chromosomCount,
      elite_strategy_count: eliteStrategyCount,
      bits_count: bitsCount,
      cross_probablility: crossProbablility,
      mutation_probability: mutationProbability,
      inversion_probability: inversionProbability,
      selection_method: selectionMethod,
      cross_method: crossMethod,
      mutation_method: mutationMethod,
    }).then(res => setResponse(res.data));

    calculationFormSubmit(setIsModalOpened);
  };

  return (
    <Container className="mt-3">
      <Row>
        <Col
          sm={{
            offset: 3,
            size: '6',
          }}
        >
          <InitialCalculationDataForm
            onFormSubmit={onFormSubmit}
            beginOfrRange={beginOfrRange}
            setBeginOfRange={setBeginOfRange}
            endOfRange={endOfRange}
            setEndOfRange={setEndOfRange}
            populationMembersCount={populationMembersCount}
            setPopulationMembersCount={setPopulationMembersCount}
            epochsCount={epochsCount}
            setEpochsCount={setEpochsCount}
            chromosomCount={chromosomCount}
            setChromosomCount={setChromosomCount}
            eliteStrategyCount={eliteStrategyCount}
            bitsCount={bitsCount}
            crossProbablility={crossProbablility}
            mutationProbability={mutationProbability}
            inversionProbability={inversionProbability}
            setEliteStrategyCount={setEliteStrategyCount}
            setInversionProbability={setInversionProbability}
            setMutationProbability={setMutationProbability}
            selectionMethod={selectionMethod}
            setSelectionMethod={setSelectionMethod}
            crossMethod={crossMethod}
            setCrossMethod={setCrossMethod}
            mutationMethod={mutationMethod}
            setMutationMethod={setMutationMethod}
            setBitsCount={setBitsCount}
            setCrossProbablility={setCrossProbablility}
          />
          <ResultModal isModalOpened={isModalOpened} hideModal={hideModal} response={response}/>
        </Col>
      </Row>
    </Container>
  );
};

export default App;
