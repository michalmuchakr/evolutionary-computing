import {Button, Col, Form, Row} from 'reactstrap';
import {initialCalculationDataFormType} from '../types/common';
import InputElement from './InputElement';
import SelectElement from "./SelectElement";

const InitialCalculationDataForm = ({
                                      onFormSubmit,
                                      beginOfrRange,
                                      setBeginOfRange,
                                      endOfRange,
                                      setEndOfRange,
                                      populationMembersCount,
                                      setPopulationMembersCount,
                                      epochsCount,
                                      setEpochsCount,
                                      chromosomCount,
                                      eliteStrategyCount,
                                      setEliteStrategyCount,
                                      setChromosomCount,
                                      inversionProbability,
                                      setInversionProbability,
                                      mutationProbability,
                                      setMutationProbability,
                                      crossProbablility,
                                      setCrossProbablility,
                                      bitsCount,
                                      setBitsCount,
                                      selectionMethod,
                                      setSelectionMethod,
                                      crossMethod,
                                      setCrossMethod,
                                      mutationMethod,
                                      setMutationMethod
                                    }: initialCalculationDataFormType) => {
  return (
    <Form onSubmit={onFormSubmit}>
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
        elementName="populationMembersCount"
        labelTxt="Population members"
        inputValue={populationMembersCount}
        onChangeCallBack={setPopulationMembersCount}
      />
      <InputElement
        elementName="bitsCount"
        labelTxt="Bits count"
        inputValue={bitsCount}
        onChangeCallBack={setBitsCount}
      />
      <InputElement
        elementName="epochsCount"
        labelTxt="Epochs amount"
        inputValue={epochsCount}
        onChangeCallBack={setEpochsCount}
      />
      <InputElement
        elementName="chromosomCount"
        labelTxt="Best and tournament chromosome amount"
        inputValue={chromosomCount}
        onChangeCallBack={setChromosomCount}
      />
      <InputElement
        elementName="eliteStrategyCount"
        labelTxt="Elite strategy amount"
        inputValue={eliteStrategyCount}
        onChangeCallBack={setEliteStrategyCount}
      />
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
      <SelectElement label="Selection method" options={['best', 'elite', 'roulette']} onChangeCallBack={setSelectionMethod} selectValue={selectionMethod}/>
      <SelectElement label="Cross method" options={['one_point', 'two_point', 'three_point', 'homo']}  onChangeCallBack={setCrossMethod} selectValue={crossMethod}/>
      <SelectElement label="Mutation method" options={['one_point', 'two_point']}  onChangeCallBack={setMutationMethod} selectValue={mutationMethod}/>
      <Row>
        <Col
          className="d-flex justify-content-center"
          md={{
            offset: 3,
            size: 6,
          }}
          sm="12"
        >
          <Button>Calculate</Button>
        </Col>
      </Row>
    </Form>
  );
};

export default InitialCalculationDataForm;
