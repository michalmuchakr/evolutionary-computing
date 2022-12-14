import {FormEvent, useEffect, useState} from 'react';
import {Col, Container, Row} from 'reactstrap';
import InitialCalculationDataForm from './components/InitialCalculationDataForm';
import ResultModal from './components/ResultModal';
import axios from "axios";

const App = () => {
  const [geneType, setGeneType] = useState('binary');
  const [problemToBeSolved, setProblemToBeSolved] = useState('minimization');
  const [beginOfrRange, setBeginOfRange] = useState('-2');
  const [endOfRange, setEndOfRange] = useState('2');
  const [populationMembersCount, setPopulationMembersCount] = useState('200');
  const [epochsCount, setEpochsCount] = useState('1000');
  const [tournamentSelectionCount, setTournamentSelectionCount] = useState('2');
  const [eliteStrategyPercentage, setEliteStrategyPercentage] = useState('20');
  const [bestMembersSelectionPercentage, setBestMembersSelectionPercentage] = useState('20');
  const [crossProbablility, setCrossProbablility] = useState('20');
  const [mutationProbability, setMutationProbability] = useState('80');
  const [inversionProbability, setInversionProbability] = useState('80');
  const [selectionMethod, setSelectionMethod] = useState('best');
  const [crossMethod, setCrossMethod] = useState('one_point');
  const [mutationMethod, setMutationMethod] = useState('homogeneous_mutation');

  const [isModalOpened, setIsModalOpened] = useState(false);
  const [isLoading, setLoading] = useState(false);

  const [backendError, setBackendError] = useState(null);
  const [response, setResponse] = useState<{
    x1: string,
    x2: string,
    fitFunVal: string
    executionTime: string;
  } | null>(null);

  const hideModal = () => {
    setIsModalOpened(false);
  };

  useEffect(() => {
    if (geneType === 'binary') {
      setCrossMethod('one_point')
      setMutationMethod('homogeneous_mutation')
    } else {
      setCrossMethod('arithmeticCrossover')
      setMutationMethod('uniform_mutation')
    }
  }, [geneType])

  const onFormSubmit = (e: FormEvent) => {
    e.preventDefault();
    setBackendError(null)
    setLoading(true);

    axios.post('http://127.0.0.1:8000/evolutionary-computing/compute/', {
      gene_type: geneType,
      epoch_amount: epochsCount,
      best_members_selection_percentage: bestMembersSelectionPercentage,
      population_members_count: populationMembersCount,
      search_result_range_from: beginOfrRange,
      search_result_range_to: endOfRange,
      elite_percentage: eliteStrategyPercentage,
      tournament_selection_groups_size: tournamentSelectionCount,
      cross_probability: crossProbablility,
      mutation_probability: mutationProbability,
      inversion_probability: inversionProbability,
      selection_method: selectionMethod,
      crossing_kind: crossMethod,
      mutation_method: mutationMethod,
      problem_to_solve: problemToBeSolved
    }).then(res => setResponse(res.data))
      .catch(e => {
        setBackendError(e.code)
      })
      .finally(() => {
        setLoading(false);
      });

    setIsModalOpened(true);
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
            problemToBeSolved={problemToBeSolved}
            setProblemToBeSolved={setProblemToBeSolved}
            bestMembersSelectionPercentage={bestMembersSelectionPercentage}
            setBestMembersSelectionPercentage={setBestMembersSelectionPercentage}
            beginOfrRange={beginOfrRange}
            setBeginOfRange={setBeginOfRange}
            endOfRange={endOfRange}
            setEndOfRange={setEndOfRange}
            populationMembersCount={populationMembersCount}
            setPopulationMembersCount={setPopulationMembersCount}
            epochsCount={epochsCount}
            setEpochsCount={setEpochsCount}
            tournamentSelectionCount={tournamentSelectionCount}
            eliteStrategyPercentage={eliteStrategyPercentage}
            // bitsCount={bitsCount}
            crossProbablility={crossProbablility}
            mutationProbability={mutationProbability}
            inversionProbability={inversionProbability}
            setEliteStrategyPercentage={setEliteStrategyPercentage}
            setInversionProbability={setInversionProbability}
            setMutationProbability={setMutationProbability}
            selectionMethod={selectionMethod}
            setSelectionMethod={setSelectionMethod}
            crossMethod={crossMethod}
            setCrossMethod={setCrossMethod}
            mutationMethod={mutationMethod}
            setMutationMethod={setMutationMethod}
            // setBitsCount={setBitsCount}
            setCrossProbablility={setCrossProbablility}
            isLoading={isLoading}
            setTournamentSelectionCount={setTournamentSelectionCount}
            setGeneType={setGeneType}
            geneType={geneType}/>
          <ResultModal hideModal={hideModal}
                       isLoading={isLoading} isModalOpened={isModalOpened} response={response} backendError={backendError}/>
        </Col>
      </Row>
    </Container>
  );
};

export default App;
