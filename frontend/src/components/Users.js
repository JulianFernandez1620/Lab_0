import React,{useState} from 'react'

const API = process.env.REACT_APP_API;

export const Users = () => {

    const [name, setName] = useState(' ')
    const [phone, setPhone] = useState(' ')

    const handleSubmit = async (e) => {
        e.preventDefault()
        const res = await fetch(`${API}/insert/usuario` , {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                name,
                phone   
            })
        })
        const data = await res.json()  
        console.log(data)   
    }

    return(
        <div className="row">
            <div className="col-md-4">
                <form onSubmit={handleSubmit} className="card card-body">
                    <div className="form-group">
                        <input 
                            type="text" 
                            onChange={e => setName(e.target.value)} 
                            value={name}
                            className="form-control"
                            placeholder="Name"
                            autoFocus                
                        />
                    </div>
                    <div className='form-group'>
                        <input 
                            type="phone" 
                            onChange={e => setPhone(e.target.value)} 
                            value={phone}
                            className='form-control'
                            placeholder="Phone"
                        />
                    </div>
            
                    <button className='btn btn-primary btn-block'>
                        Crear
                    </button>
                </form>
            </div>
            <div className='col-md-8'>

            </div>

        </div>
    )
}