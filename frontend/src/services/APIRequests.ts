import { TransactionCategoryType, TransactionType } from "../data/types/Index";

export const getUsersWallets = async (accessToken: string | null, handleError: () => void) => {
    const response = await fetch('http://127.0.0.1:8000/api/wallets/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + accessToken
        }
    })

    
    if(response.status === 200) {
        const responseJSON = await response.json();
        return responseJSON
    }

    if(response.statusText === 'Unauthorized') {
        handleError();
    }
}

export const getWalletsTransactions = async (accessToken: string | null, id: number, handleError: () => void) => {
    const response = await fetch(`http://127.0.0.1:8000/api/wallet/transactions/${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + accessToken
        }
    })

    
    if(response.status === 200) {
        const responseJSON = await response.json();
        const transactionsArray = responseJSON.map((row: any) => {
            let transaction: TransactionType = {
                id: row.id,
                name: row.name,
                value: row.value,
                description: row.description,
                recipient: row.recipient,
                date: new Date(row.date),
                categoryID: row.category,
                operationTypeID: row.operationType,
                walletID: row.wallet,
            }

            return transaction
        })
        return transactionsArray
    }

    if(response.statusText === 'Unauthorized') {
        handleError();
    }
}

export const getWalletsTransactionCategories = async (accessToken: string | null, id: number, handleError: () => void) => {
    const response = await fetch(`http://127.0.0.1:8000/api/wallet/transaction_categories/${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + accessToken
        }
    })

        if(response.status === 200) {
        const responseJSON = await response.json();
        const transactionsArray = responseJSON.map((row: any) => {
            let transactionCategory: TransactionCategoryType = {
                id: row.id,
                name: row.name,
                walletId: row.wallet,
                operationTypeId: row.operationType
            }
            return transactionCategory
        })
        return transactionsArray
    }

    if(response.statusText === 'Unauthorized') {
        handleError();
    }
}

export const getWalletsCategories = async (accessToken: string | null, id: number, handleError: () => void) => {
    const response = await fetch(`http://127.0.0.1:8000/api/wallet/categories/${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + accessToken
        }
    })

    
    if(response.status === 200) {
        const responseJSON = await response.json();
        // const transactionsArray = responseJSON.map((row: any) => {
        //     let transaction: TransactionType = {
        //         id: row.id,
        //         value: row.value,
        //         description: row.description,
        //         recipient: row.recipient,
        //         date: new Date(row.date),
        //         categoryID: row.category,
        //         transactionTypeID: row.transaction_type,
        //         walletID: row.wallet,

        //     }

        //     return transaction
        // })
        // return transactionsArray

        return responseJSON
    }

    if(response.statusText === 'Unauthorized') {
        handleError();
    }
}
