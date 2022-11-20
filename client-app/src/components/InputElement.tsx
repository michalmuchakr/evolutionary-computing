import { Dispatch, FormEvent, SetStateAction } from 'react';
import { Col, FormGroup, Input, Label } from 'reactstrap';
import { InputType } from 'reactstrap/types/lib/Input';

const InputElement = ({
  labelTxt,
  elementName,
  placeholder,
  inputType = 'text',
  inputValue,
  onChangeCallBack,
}: {
  labelTxt: string;
  elementName: string;
  placeholder?: string;
  inputType?: InputType;
  inputValue: string;
  onChangeCallBack: Dispatch<SetStateAction<string>>;
}) => {
  const onInputChange = (e: FormEvent<HTMLInputElement>) => {
    if (onChangeCallBack) {
      const updatedValue = e.currentTarget.value;
      onChangeCallBack(updatedValue);
    }
  };

  return (
    <FormGroup row className="mt-3">
      <Label for={elementName} sm={4}>
        {labelTxt}
      </Label>
      <Col sm={8}>
        <Input
          id={elementName}
          name={elementName}
          placeholder={placeholder}
          type={inputType}
          value={inputValue}
          onChange={onInputChange}
        />
      </Col>
    </FormGroup>
  );
};

export default InputElement;
