import {Col, FormGroup, Input, Label} from "reactstrap";
import {Dispatch, FormEvent, SetStateAction} from "react";

const SelectElement = ({label, options, onChangeCallBack, selectValue}: {
  label: string;
  options: string[],
  onChangeCallBack: Dispatch<SetStateAction<string>>;
  selectValue: string;
}) => {
  const onSelectChange = (e: FormEvent<HTMLInputElement>) => {
    const updatedValue = e.currentTarget.value;
    onChangeCallBack(updatedValue);
  };

  return (
    <FormGroup row className="mt-3">
      <Label for="exampleSelect" sm={4}>{label}</Label>

      <Col sm={8}>
        <Input type="select" name="select" id="exampleSelect" onChange={onSelectChange} value={selectValue}>
          {options.map((optionsItem: string) => (
              <option key={optionsItem}>{optionsItem}</option>
            )
          )}
        </Input>
      </Col>
    </FormGroup>
  );
};

export default SelectElement;