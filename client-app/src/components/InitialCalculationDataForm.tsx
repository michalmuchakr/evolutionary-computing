import {Button, Col, Form, Row} from 'reactstrap';
import {initialCalculationDataFormType} from '../types/common';
import InputElement from './InputElement';
import SelectElement from "./SelectElement";

const InitialCalculationDataForm = ({
                                      problemToBeSolved,
                                      setProblemToBeSolved,
                                      bestMembersSelectionPercentage,
                                      setBestMembersSelectionPercentage,
                                      onFormSubmit,
                                      beginOfrRange,
                                      setBeginOfRange,
                                      endOfRange,
                                      setEndOfRange,
                                      populationMembersCount,
                                      setPopulationMembersCount,
                                      epochsCount,
                                      setEpochsCount,
                                      tournamentSelectionCount,
                                      setTournamentSelectionCount,
                                      eliteStrategyPercentage,
                                      setEliteStrategyPercentage,
                                      inversionProbability,
                                      setInversionProbability,
                                      mutationProbability,
                                      setMutationProbability,
                                      crossProbablility,
                                      setCrossProbablility,
                                      selectionMethod,
                                      setSelectionMethod,
                                      crossMethod,
                                      setCrossMethod,
                                      mutationMethod,
                                      setMutationMethod,
                                      isLoading
                                    }: initialCalculationDataFormType) => {
  return (
    <Form onSubmit={onFormSubmit}>
      <SelectElement label="Problem to solve" options={['minimization', 'maximization']}
                     onChangeCallBack={setProblemToBeSolved} selectValue={problemToBeSolved}/>
      <InputElement
        elementName="epochsCount"
        labelTxt="Epochs amount"
        inputValue={epochsCount}
        onChangeCallBack={setEpochsCount}
      />
      <InputElement
        elementName="populationMembersCount"
        labelTxt="Population members"
        inputValue={populationMembersCount}
        onChangeCallBack={setPopulationMembersCount}
      />
      <InputElement
        elementName="beginOfrRange"
        labelTxt="Begin of range"
        inputValue={beginOfrRange}
        onChangeCallBack={setBeginOfRange}
      />
      <InputElement
        elementName="endOfRange"
        labelTxt="End of range"
        inputValue={endOfRange}
        onChangeCallBack={setEndOfRange}
      />
      <InputElement
        elementName="eliteStrategyPercentage"
        labelTxt="Elite strategy percentage"
        inputValue={eliteStrategyPercentage}
        onChangeCallBack={setEliteStrategyPercentage}
      />
      {/*<InputElement*/}
      {/*  elementName="bestMembersSelectionPercentage"*/}
      {/*  labelTxt="Best members percentage"*/}
      {/*  inputValue={bestMembersSelectionPercentage}*/}
      {/*  onChangeCallBack={setBestMembersSelectionPercentage}*/}
      {/*/>*/}
      {/*<InputElement*/}
      {/*  elementName="chromosomCount"*/}
      {/*  labelTxt="Tournament selection amount"*/}
      {/*  inputValue={tournamentSelectionCount}*/}
      {/*  onChangeCallBack={setTournamentSelectionCount}*/}
      {/*/>*/}
      <InputElement
        elementName="crossProbablility"
        labelTxt="Cross probablility"
        inputValue={crossProbablility}
        onChangeCallBack={setCrossProbablility}
      />
      <InputElement
        elementName="mutationProbability"
        labelTxt="Mutation probability"
        inputValue={mutationProbability}
        onChangeCallBack={setMutationProbability}
      />
      <InputElement
        elementName="inversionProbability"
        labelTxt="Inversion probability"
        inputValue={inversionProbability}
        onChangeCallBack={setInversionProbability}
      />
      <SelectElement label="Selection method" options={['best', 'roulette', 'tournament']} onChangeCallBack={setSelectionMethod}
                     selectValue={selectionMethod}/>
      <SelectElement label="Cross method" options={['one_point', 'two_points', 'three_point', 'homo']}
                     onChangeCallBack={setCrossMethod} selectValue={crossMethod}/>
      <SelectElement label="Mutation method" options={['homogeneous_mutation', 'edge_mutation', 'two_point_mutation']} onChangeCallBack={setMutationMethod}
                     selectValue={mutationMethod}/>
      <Row>
        <Col
          className="d-flex justify-content-center"
          md={{
            offset: 3,
            size: 6,
          }}
          sm="12"
        >
          <Button
            disabled={isLoading}
            type="submit"
          >
            {isLoading ? 'Loading…' : 'Calculate'}
          </Button>
        </Col>
      </Row>
    </Form>
  );
};

export default InitialCalculationDataForm;
